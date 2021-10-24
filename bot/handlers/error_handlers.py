import logging
from bot.config import LOGGING_FORMAT


logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def error_handler(update, context):
    logging.info("DEBUGGER: caused error, {}".format(context.error))
    return
