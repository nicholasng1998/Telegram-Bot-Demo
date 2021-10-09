from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from bot.config import LOGGING_FORMAT
import time
import logging

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def catalog(update, context):
    logging.info("User: Press Catalog")
    keyboard = [
        [InlineKeyboardButton('🍕 Pizza', callback_data='pizza'), InlineKeyboardButton('🥖 Sticks', callback_data='sticks')],
        [InlineKeyboardButton('🍹 Beverages', callback_data='beverages')]
    ]

    reply_text = "📒 Catalog \nThis is the main directory"
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def pizza(update, context):
    logging.info("User: Press 🍕 Pizza")
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Large 14', switch_inline_query_current_chat="pizza large"),
         InlineKeyboardButton('Medium 12', switch_inline_query_current_chat='pizza medium')],
        [InlineKeyboardButton('Small 9', switch_inline_query_current_chat='pizza small')]
    ]

    reply_text = "Choose your pizza size: "
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def sticks(update, context):
    logging.info("User: Press 🥖 Sticks")
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Garlic Twisty Bread', switch_inline_query_current_chat="garlic twisty bread"),
         InlineKeyboardButton('Cheesy Cheddar Stix', switch_inline_query_current_chat="chessy cheddar stix")]
    ]

    reply_text = "Choose your stix: "
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def beverages(update, context):
    logging.info("User: Press 🍹 Beverages")
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Soda', switch_inline_query_current_chat="soda")]
    ]

    reply_text = "Choose your drinks: "
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def large(update, context):
    update.callback_query.message.reply_text('large')


def medium(update, context):
    update.message.reply_text('medium')


def small(update, context):
    update.message.reply_text('small')


def add_cart(update, context):
    context.user_data['cart'].append(update.callback_query.data)


def place_order(update, context):
    context.user_data['addressRequired'] = True
    update.callback_query.message.reply_text('Please send me your address as example below. (Address: No 1, Lorong ..)')


def retype(update, context):
    place_order(update, context)


def confirm(update, context):
    callback_data = update.callback_query.data
    address = str(callback_data).replace("confirmAddress", '')
    context.user_data['address'] = address
    reply_text = 'Select a Payment Method'
    keyboard = [
        [InlineKeyboardButton('Cash to the courier', callback_data='cashToCourier')]
    ]
    context.user_data['addressRequired'] = False
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text,
                             reply_markup=InlineKeyboardMarkup(keyboard))


def cash_to_courier(update, context):
    context.user_data['payment_method'] = 'Cash to Courier'
    context.user_data['commentRequired'] = True
    reply_text = 'Please write a comment to the order: For example, an additional telephone number for contacting.'
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text)


def cancel(update, context):
    reply_text = 'order cancelled'
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text)


def accept(update, context):
    reply_text = 'order placed'
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text)
    time.sleep(2)
    context.bot.send_message(chat_id=update.effective_user.id, text="Your order is transferred to the assembly!")
    time.sleep(2)
    context.bot.send_message(chat_id=update.effective_user.id, text="Your order has been submitted for delivery!")
    time.sleep(2)
    context.bot.send_message(chat_id=update.effective_user.id,
                             text="Your order has been successfully delivered! Thank you for using our service. Do not forget to share with your friend.")
