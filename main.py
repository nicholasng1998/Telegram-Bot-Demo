from telegram.ext import *
from bot import config
import pathlib
from bot.utils import image
from bot.config import LOGGING_FORMAT
import logging
from bot.handlers import (
    command_handlers,
    error_handlers,
    message_handlers,
    photo_handlers,
    inlinequery_handlers,
    callbackquery_handlers
)

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)

def main():
    # use_context is for backward compatibility
    updater = Updater(config.API_KEY, use_context=True)

    # access dispatcher
    dp = updater.dispatcher

    # add command handlers
    dp.add_handler(CommandHandler("start", command_handlers.start))
    dp.add_handler(CommandHandler("help", command_handlers.helps))

    # add message handlers
    dp.add_handler(MessageHandler(Filters.text, message_handlers.handle))
    dp.add_handler(MessageHandler(Filters.photo, photo_handlers.handle))

    # add inline query handler
    dp.add_handler(InlineQueryHandler(inlinequery_handlers.inline_query))

    # add callback query handler
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.catalog, pattern="catalog"))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.type_handlers, pattern="^type."))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.add_cart, pattern="^addToCart."))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.place_order, pattern='placeOrder'))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.retype, pattern='retype'))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.confirm, pattern='^confirmAddress'))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cash_to_courier, pattern='cashToCourier'))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cancel, pattern='cancel'))
    # dp.add_handler(CallbackQueryHandler(callbackquery_handlers.accept, pattern='accept'))

    updater.dispatcher.add_error_handler(error_handlers.error_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
