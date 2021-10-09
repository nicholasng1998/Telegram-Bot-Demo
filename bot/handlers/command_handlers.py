from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup
)
from bot import constant
from bot.utils import bot

"""
    Emoji can be found from url below:
    https://www.iemoji.com/
"""


def start(update, context):
    bot.init(context)

    # MxN matrix that able to arrange button
    keyboard_buttons = [
        [KeyboardButton(constant.CATALOG), KeyboardButton(constant.CART)],
        [KeyboardButton(constant.MY_PROFILE), KeyboardButton(constant.ORDER_HISTORY)]
    ]

    update.message.reply_text(
        constant.GREETING_MESSAGE,
        reply_markup=ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)
    )


def helps(update, context):
    update.message.reply_text(constant.HELP_MESSAGE)
