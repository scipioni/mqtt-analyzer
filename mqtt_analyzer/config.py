from typing import Any
import configargparse


def get_config() -> Any:
    parser = configargparse.get_argument_parser()

    parser.add_argument("--host", default="10.45.103.1")
    parser.add_argument("--port", default=1884)
    parser.add_argument("--out", default="/tmp/gps.csv")
    parser.add_argument("--test", default="")
    return parser.parse_args()
