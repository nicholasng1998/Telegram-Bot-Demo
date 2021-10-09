from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ChatAction
)
from bot import constant
from bot.utils import bot
from bot.config import LOGGING_FORMAT
import time
import logging

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def start(update, context):
    logging.info("User: /start")
    bot.init(context)

    # MxN matrix that able to arrange button
    keyboard_buttons = [
        [KeyboardButton(constant.CATALOG), KeyboardButton(constant.CART)],
        [KeyboardButton(constant.MY_PROFILE), KeyboardButton(constant.ORDER_HISTORY)]
    ]

    # sending chat action Typing...
    chat_id = update.effective_user.id
    telegram_bot = context.bot
    telegram_bot.sendChatAction(chat_id=chat_id, action=ChatAction.TYPING)
    time.sleep(0.5)

    logging.info("Bot: " + constant.GREETING_MESSAGE)
    update.message.reply_text(
        constant.GREETING_MESSAGE,
        reply_markup=ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)
    )


def helps(update, context):
    logging.info("User: /help")

    # sending chat action Typing...
    chat_id = update.effective_user.id
    telegram_bot = context.bot
    telegram_bot.sendChatAction(chat_id=chat_id, action=ChatAction.TYPING)
    time.sleep(0.5)

    logging.info("Bot: " + constant.HELP_MESSAGE)
    update.message.reply_text(constant.HELP_MESSAGE)
