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


def pizza_menu(bot, context):
    print(bot)
    print(dir(bot))
    print(type(bot))
    print(type(bot.callback_query))
    print(type(bot.callback_query.message))
    file_path = pathlib.Path("images/doctor strange.jpg")
    if file_path.exists():
        print('asdasd')
        print("type: {}".format(type(file_path)))
        # photo = file_path
        # photo = "C:/workspace/telegramBot/images/doctor strange.jpg"
        # bot.send_photo(photo=photo)
        # print("type: {}".format(type(photo)))
        # with open("images/doctor strange.jpg", "rb") as image:
        #     f = image.read()
        #     b = bytearray(f)
        # photo1 = InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")
        # photo2 = InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")
        # photo3 = InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")
        # photo4 = InputMediaPhoto("https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")
        # image_file = open("images/doctor strange.jpg", 'rb')
        # image_byte = image_file.read()
        # image_file.close()
        # photo1 = InputMediaPhoto(image_byte)
        photo1 = image.upload_local_photo("images/doctor strange.jpg")
        bot.callback_query.message.reply_media_group([photo1])
        # bot.callback_query.message.reply_photo(photo="https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")
    print("no la")
    # bot.callback_query.message.reply_text('Choose a date:',
    #                                      photo_url="https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg")


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
