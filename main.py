from telegram.ext import *
from bot import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, KeyboardButton
from telegramCalendar import telegramcalendar
from telegram.files.photosize import PhotoSize
from telegram.utils.types import FileInput
import pathlib
import io
from PIL import Image
from bot.utils import image
from bot.config import LOGGING_FORMAT
import logging
from bot.handlers import (
    command_handlers,
    message_handlers,
    inlinequery_handlers,
    callbackquery_handlers
)

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


# def first_menu_keyboard():
#
#     keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
#                 [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
#                 [InlineKeyboardButton('Main menu', callback_data='main')]]
#     return InlineKeyboardMarkup(keyboard)
#
#
# def second_menu_keyboard():
#     keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
#                 [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
#                 [InlineKeyboardButton('Main menu', callback_data='main')]]
#     return InlineKeyboardMarkup(keyboard)

# def cal(bot, update):
#     result, key, step = DetailedTelegramCalendar().process(bot.data)
#     if not result and key:
#         bot.edit_message_text(f"Select {LSTEP[step]}",
#                               bot.message.chat.id,
#                               bot.message.message_id,
#                               reply_markup=key)
#     elif result:
#         bot.edit_message_text(f"You selected {result}",
#                               bot.message.chat.id,
#                               bot.message.message_id)

# def first_menu(bot, update):
#     print(bot)
#     print(dir(bot))
#     telegramCalendar, step = DetailedTelegramCalendar().build()
#     bot.callback_query.message.edit_text(first_menu_message(),
#                      reply_markup=telegramCalendar)
    # bot.callback_query.message.edit_text(first_menu_message(),
    #                                      reply_markup=first_menu_keyboard())


# def second_menu(bot, update):
#     bot.callback_query.message.edit_text(second_menu_message(),
#                                          reply_markup=second_menu_keyboard())

# def error(update, context):
#     print(f'Update {update} caused error {context.error}')

def start_command(update, context):
    keyboard = KeyboardButton(text='button here')
    update.message.reply_text(text='asd', reply_markup=keyboard)
    # update.message.reply_text("Welcome to Test Bot")


def help_command(update, context):
    update.message.reply_text()


def booking_keyboard():
    keyboard = [[InlineKeyboardButton('pizza', callback_data='pizza')],
                [InlineKeyboardButton('cookie', callback_data='cookie')],
                [InlineKeyboardButton('kfc', callback_data='kfc')]]
    return InlineKeyboardMarkup(keyboard)


def booking_command(bot, update):
    print(bot)
    print(dir(bot))
    print(type(bot))
    print(type(bot.message))
    bot.message.reply_text('Choose the package below:',
                           reply_markup=booking_keyboard())


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

    # add inline query handler
    dp.add_handler(InlineQueryHandler(inlinequery_handlers.inline_query, pass_user_data=True))

    # add callback query handler
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.catalog, pattern='catalog'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.pizza, pattern='pizza'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.sticks, pattern='sticks'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.beverages, pattern='beverages'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.large, pattern='large'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.medium, pattern='medium'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.small, pattern='small'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.add_cart, pattern='^addToCart'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.place_order, pattern='placeOrder'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.retype, pattern='retype'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.confirm, pattern='^confirmAddress'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cash_to_courier, pattern='cashToCourier'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.cancel, pattern='cancel'))
    dp.add_handler(CallbackQueryHandler(callbackquery_handlers.accept, pattern='accept'))

    # updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
