import logging
import argparse
import os
from telegram.ext import *
from bot import config
from bot.config import LOGGING_FORMAT, API_TOKEN, BOT_1, BOT_ID, API_KEY
from bot.handlers import (
    command_handlers,
    error_handlers,
    message_handlers,
    photo_handlers,
    inlinequery_handlers,
    callbackquery_handlers
)

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def main(active_profile: str):
    # use_context is for backward compatibility
    updater = Updater(API_KEY, use_context=True)

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
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.remove_item, pattern="removeItem"))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.remove_item_by_id, pattern="^removeById."))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.place_order, pattern='placeOrder'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.retype_address, pattern='retype'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.confirm_address, pattern='^confirmAddress'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cash_to_courier, pattern='cashToCourier'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cancel_order, pattern='cancelOrder'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.accept_order, pattern='acceptOrder'))

    updater.dispatcher.add_error_handler(error_handlers.error_handler)
    if active_profile == "local":
        updater.start_polling()
    elif active_profile == "production":
        logging.info("start web hook...")
        updater.start_webhook(listen="0.0.0.0",
                              port=int(os.environ.get('PORT', '8443')),
                              url_path=API_KEY,
                              webhook_url="https://nicholas-telegram-bot-demo.herokuapp.com/" + API_KEY)
    updater.idle()


if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description='Profile')
    parser.add_argument("--profile", type=str, default="local", help="Write your profile.")
    active_profile = parser.parse_args().profile
    logging.info("Active profile: {}".format(active_profile))
    main(active_profile)
