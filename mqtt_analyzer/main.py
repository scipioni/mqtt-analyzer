import json
import logging

import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


"""
2022-11-11T17:51:59.533121+00:00,50313953666c4750,adeinus-ftd_1,45.4382,11.008166666666666,-114,-4.5
"""


class Mock:
    topic = ""
    payload = ""


class Analyzer:
    # The callback for when the client receives a CONNACK response from the server.

    def __init__(self, config):
        self.config = config
        self.f = open(self.config.out, "a")

    def on_connect(self, client, userdata, flags, rc):
        log.info("Connected with result code: %s", rc)
        client.subscribe("application/#")

    def on_message(self, client, userdata, msg):
        log.info("%s: %s", msg.topic, msg.payload)

        try:
            message = json.loads(msg.payload.decode())
            self.parse_message(message)
        except Exception as e:
            log.error(str(e))

    def connect(self):
        log.info("connecting ...")
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(self.config.host, port=self.config.port, keepalive=60)
        client.loop_forever()

    def parse_message(self, message):
        id = message["deduplicationId"]
        for rx in message["rxInfo"]:
            obj = message["object"]
            out = f"{rx['time']},{message['deviceInfo']['deviceName']},{obj['latitude']},{obj['longitude']},{rx['rssi']},{rx['snr']},{rx['gatewayId']},{id}"
            log.info(out)
            self.f.write(out + "\n")
            self.f.flush()

    def test(self):
        mock = Mock()
        mock.payload = b'{"deduplicationId":"89ad3d4f-f112-41d8-96f4-79ddfdfab773","time":"2023-02-02T08:04:41.586413+00:00","deviceInfo":{"tenantId":"52f14cd4-c6f1-4fbd-8f87-4025e1d49242","tenantName":"ChirpStack","applicationId":"b569c92f-53bd-41d3-85f3-c1ca77e929f4","applicationName":"test-device","deviceProfileId":"4d17a2b5-9066-4ddd-8be9-09909e64e24c","deviceProfileName":"FTD Network Tester","deviceName":"adeinus-ftd_1","devEui":"0018b200000262b0"},"devAddr":"00ca2ece","fCnt":238,"fPort":1,"data":"nhRFJnkAARACYBbuqw2z","object":{"latitude":45.4465,"downlink":171.0,"uplink":238.0,"battery":3507.0,"temperature":20.0,"longitude":11.004333333333333,"altitude":0.0,"sats":6.0},"rxInfo":[{"gatewayId":"5031395366684750","uplinkId":20737,"time":"2023-02-02T08:04:41.586413+00:00","rssi":-115,"snr":-0.25,"channel":4,"location":{"latitude":45.437981,"longitude":10.994118,"altitude":83.0},"context":"JDSCxA==","metadata":{"region_common_name":"EU868","region_name":"eu868"}}],"txInfo":{"frequency":867300000,"modulation":{"lora":{"bandwidth":125000,"spreadingFactor":12,"codeRate":"CR_4_5"}}}}'
        mock.topic = "application/b569c92f-53bd-41d3-85f3-c1ca77e929f4/device/0018b200000262b0/event/up"
        self.on_message(None, None, mock)


def main():
    from .config import get_config

    config = get_config()

    analyzer = Analyzer(config)
    if config.test:
        analyzer.test()
    else:
        analyzer.connect()
