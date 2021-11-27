import logging
from bot.config import LOGGING_FORMAT

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def handle(update, context):
    print(update)
    logging.info("DEBUGGER: Enter photo handlers")
