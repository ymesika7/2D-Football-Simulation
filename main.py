import logging
import logging.config
from cli import Cli
from config import LOG_CONF


def main():
    logging.config.fileConfig(LOG_CONF)
    cli=Cli()
    cli.parse_arguments_advanced()
    cli.args_handel()


if __name__ == '__main__':
    main()