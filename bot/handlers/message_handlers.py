from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    ChatAction
)
from bot import constant
from bot.config import LOGGING_FORMAT
import logging
import time

# main menu
CATALOG = "📒 Catalog"
ORDER_HISTORY = "📄 Order History"
MY_PROFILE = "👤 My Profile"
CART = "🛒 Cart"

# catalog sub menu
PIZZA = 'Pizza'
STICKS = 'Sticks'
BEVERAGES = 'Beverages'

PIZZAS = [
    'Buffalo Chicken Mac N Cheese (L)$5.00',
    'Ragin Pepperoni (L)$5.00',
    'Mac n Cheese (L)$5.00'
]

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def handle(update, context):

    user_text = update.message.text
    logging.info("User: " + user_text)

    # catalog button pressed
    if CATALOG == user_text:
        catalog_button_response(update, context)

    # cart button pressed
    elif CART == user_text:
        cart_button_response(update, context)

    elif user_text in PIZZAS:
        logging.info("selected pizza: " + user_text)

    elif context.user_data[constant.ADDRESS_REQUIRED]:
        reply_text = 'Your address is: ' + user_text
        keyboard = [
            [InlineKeyboardButton('Retype', callback_data='retype'),
             InlineKeyboardButton('Confirm', callback_data='confirmAddress' + user_text)]
        ]
        update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif context.user_data[constant.COMMENT_REQUIRED]:
        context.user_data['comment_text'] = user_text
        summary = '''
        Your order
        Cart: ''' + ', '.join(context.user_data['cart']) \
                  + "Address: " + context.user_data['address'] \
                  + "Payment Method: " + context.user_data['payment_method'] \
                  + "Comment: " + context.user_data['comment_text']
        keyboard = [
            [InlineKeyboardButton('Cancel', callback_data='cancel'),
             InlineKeyboardButton('Accept', callback_data='accept')]
        ]
        context.user_data['commentRequired'] = False
        update.message.reply_text(summary, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.HTML)
    else:
        if not context.user_data:
            print('kosong')
        print('not ko song')
        update.message.reply_text(constant.COMMAND_NOT_FOUND, parse_mode=ParseMode.HTML)


def catalog_button_response(update, context):
    keyboard = [
        [InlineKeyboardButton('Gizzly Bear', callback_data='type.grizzly')],
        [InlineKeyboardButton('Ice Bear', callback_data='type.iceBear')],
        [InlineKeyboardButton('Panda Bear', callback_data='type.panda')]
    ]

    reply_text = "📒 Catalog \nThis is our main directory. Please select any type of bear below:"
    logging.info("Bot: " + reply_text)
    update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def cart_button_response(update, context):
    keyboard = [
        [InlineKeyboardButton('Clear', callback_data='clear'),
         InlineKeyboardButton('Place Order', callback_data='placeOrder')]
    ]

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.message.reply_text(reply_text)
        return

    reply_text = "Your order are listed below: \n"
    counter = 0
    logging.info("DEBUGGER: Number of orders: " + str(len(context.user_data[constant.CART_ARRAY])))
    order_text_format = "{}. {}\n"
    for order in context.user_data[constant.CART_ARRAY]:
        counter += 1
        reply_text += order_text_format.format(str(counter), order)

    logging.info("Bot: " + reply_text)
    update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))
