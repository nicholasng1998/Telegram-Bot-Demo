from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from bot import constant
from bot.config import LOGGING_FORMAT
import time
import logging

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def catalog(update, context):
    logging.info("User: Press Catalog")
    keyboard = [
        [InlineKeyboardButton('Gizzly Bear', callback_data='type.grizzly')],
        [InlineKeyboardButton('Ice Bear', callback_data='type.iceBear')],
        [InlineKeyboardButton('Panda Bear', callback_data='type.panda')]
    ]

    reply_text = "📒 Catalog \nThis is our main directory. Please select any type of bear below:"
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def pizza(update, context):
    logging.info("User: Press 🍕 Pizza")
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Large 14', switch_inline_query_current_chat="Large"),
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

    context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="processing...")

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
    add_to_cart_prefix = "addToCart:"
    logging.info("User: add to cart")

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        chat_id = update.effective_user.id

        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    callback_data = update.callback_query.data
    order = str(callback_data).replace(add_to_cart_prefix, '')

    context.user_data[constant.CART_ARRAY].append(order)
    if order in context.user_data[constant.CART_ARRAY]:
        logging.info("DEBUGGER: Added to cart successfully.")
        context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Added to cart")
    else:
        logging.info("DEBUGGER: Fail adding to cart.")
        chat_id = update.effective_user.id
        reply_text = "Fail adding to cart. Please try again."
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)


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


def type_handlers(update, context):
    callback_data = update.callback_query.data

    if callback_data is None:
        logging.info("DEBUGGER: callback data is None.")
        chat_id = update.effective_user.id

        reply_text = constant.COMMON_ERROR_MESSAGE
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    chosen_type = str(callback_data).replace("type.", "")
    logging.info("User: chosen type {}".format(chosen_type))

    keyboard = [
        [InlineKeyboardButton(constant.CATALOG, callback_data='catalog')],
        [InlineKeyboardButton('25 cm', switch_inline_query_current_chat="{} 25cm".format(chosen_type)),
         InlineKeyboardButton('30 cm', switch_inline_query_current_chat="{} 30cm".format(chosen_type))],
        [InlineKeyboardButton('40 cm', switch_inline_query_current_chat="{} 40cm".format(chosen_type)),
         InlineKeyboardButton('50 cm', switch_inline_query_current_chat="{} 50cm".format(chosen_type))]
    ]

    reply_text = "You selected {}. Please select any size of {}:".format(chosen_type, chosen_type)
    logging.info("Bot: " + reply_text)
    update.callback_query.message.edit_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))
