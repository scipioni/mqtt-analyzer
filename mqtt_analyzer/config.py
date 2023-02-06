from typing import Any
import configargparse


def get_config() -> Any:
    parser = configargparse.get_argument_parser()

    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=1883, type=int)
    parser.add_argument("--out", default="/tmp/data.csv")
    parser.add_argument("--test", action="store_true", default=False)
    parser.add_argument(
        "-c", "--config", required=False, is_config_file=True, help="config file path"
    )
    parser.add_argument(
        "--config-save",
        required=False,
        is_write_out_config_file_arg=True,
        help="config file path",
    )

    return parser.parse_args()
