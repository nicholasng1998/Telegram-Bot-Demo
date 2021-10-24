import logging
from bot.config import LOGGING_FORMAT

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def handle(update, context):
    logging.info("DEBUGGER: custom message from user -> {}".format(update.message))

