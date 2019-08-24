import argparse
from collections import namedtuple

from citizens_api.const import DEFAULT_HOST, DEFAULT_PORT


class ArgParser:
    @staticmethod
    def parse():
        ParseResult = namedtuple("ParseResult", ("rest_app_host", "rest_app_port", "is_debug"))

        parser = argparse.ArgumentParser()

        parser.add_argument("--host", action="store", dest="rest_app_host", type=str, required=False,
                            default=DEFAULT_HOST, help="Rest application host")
        parser.add_argument("--port", action="store", dest="rest_app_port", type=int, required=False,
                            default=DEFAULT_PORT, help="Rest application port")
        parser.add_argument("--debug", action="store_true", dest="is_debug", help="Debug mode")

        cli_args = parser.parse_args()

        return ParseResult(cli_args.rest_app_host, cli_args.rest_app_port, cli_args.is_debug)
