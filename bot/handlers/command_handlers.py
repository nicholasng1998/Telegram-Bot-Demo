from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ChatAction
)
from bot import constant, sql_constant
from bot.utils import bot
from bot.config import LOGGING_FORMAT
import time
import logging
import sqlite3

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def start(update, context):
    logging.info("User: /start")
    bot.init(context)

    con = sqlite3.connect("bot_data.db")
    chat_id = update.message.chat.id
    user_name = update.message.chat.first_name

    cursor_obj = con.cursor()
    cursor_obj.execute(sql_constant.SELECT_USER.format(chat_id))
    users = cursor_obj.fetchall()
    if len(users) > 0:
        user_id, name, address, chat_id = users[0]
        logging.info("User chat id: {}".format(str(chat_id)))
    elif len(users) == 0:
        insert_user_sql = sql_constant.INSERT_USER.format(user_name, "NULL", chat_id)
        cursor_obj.execute(insert_user_sql)
        con.commit()
    con.close()

    # MxN matrix that able to arrange button
    # keyboard_buttons = [
    #     [KeyboardButton(constant.CATALOG), KeyboardButton(constant.CART)],
    #     [KeyboardButton(constant.MY_PROFILE), KeyboardButton(constant.ORDER_HISTORY)]
    # ]

    keyboard_buttons = [
        [KeyboardButton(constant.CATALOG), KeyboardButton(constant.CART)]
    ]

    # sending chat action Typing...
    chat_id = update.effective_user.id
    telegram_bot = context.bot
    telegram_bot.sendChatAction(chat_id=chat_id, action=ChatAction.TYPING)

    logging.info("Bot: " + constant.GREETING_MESSAGE)
    update.message.reply_text(
        constant.GREETING_MESSAGE,
        reply_markup=ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)
    )

    telegram_bot.send_photo(chat_id=chat_id, photo=constant.POSTER_FILE_ID)


def helps(update, context):
    logging.info("User: /help")

    # sending chat action Typing...
    chat_id = update.effective_user.id
    telegram_bot = context.bot
    telegram_bot.sendChatAction(chat_id=chat_id, action=ChatAction.TYPING)
    time.sleep(0.5)

    logging.info("Bot: " + constant.HELP_MESSAGE)
    update.message.reply_text(constant.HELP_MESSAGE)
