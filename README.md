# mqtt-analyzer

## lora packet

```
{
   "deduplicationId":"8aea4e90-4383-42f6-9f3d-85e6f9072c01",
   "time":"2022-11-11T17:48:26.091813+00:00",
   "deviceInfo":{
      "tenantId":"52f14cd4-c6f1-4fbd-8f87-4025e1d49242",
      "tenantName":"ChirpStack",
      "applicationId":"b569c92f-53bd-41d3-85f3-c1ca77e929f4",
      "applicationName":"test-device",
      "deviceProfileId":"8a30f77e-a9ec-4e27-89e7-95ed6c9f5072",
      "deviceProfileName":"lt22222-l",
      "deviceName":"dragino-lt22222-l_1",
      "devEui":"a84041c21185798c"
   },
   "devAddr":"0069d015",
   "adr":true,
   "dr":5,
   "fCnt":41,
   "fPort":2,
   "data":"L9IAAAAAAAA8/0E=",
   "object":{
      "RO1_status":"OFF",
      "RO2_status":"OFF",
      "AVI1_V":12.242,
      "ACI1_mA":0.0,
      "AVI2_V":0.0,
      "DI1_status":"H",
      "Work_mode":"2ACI+2AVI",
      "ACI2_mA":0.0,
      "DI2_status":"H",
      "DO1_status":"H",
      "Hardware_mode":"LT22222",
      "DO2_status":"H"
   },
   "rxInfo":[
      {
         "gatewayId":"5031395366684750",
         "uplinkId":49153,
         "time":"2022-11-11T17:48:26.091813+00:00",
         "rssi":-17,
         "snr":9.75,
         "channel":6,
         "location":{
            "latitude":45.457221,
            "longitude":11.070229,
            "altitude":76.0
         },
         "context":"7m7wxA==",
         "metadata":{
            "region_common_name":"EU868",
            "region_name":"eu868"
         }
      }
   ],
   "txInfo":{
      "frequency":867700000,
      "modulation":{
         "lora":{
            "bandwidth":125000,
            "spreadingFactor":7,
            "codeRate":"CR_4_5"
         }
      }
   }
}
```