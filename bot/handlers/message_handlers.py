from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode
)
import re
from bot import constant

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


def handle(update, context):
    user_text = str(update.message.text).lower()
    print(user_text)
    if CATALOG.lower() in user_text:
        keyboard = [
            [InlineKeyboardButton('Pizza', callback_data='pizza'), InlineKeyboardButton('Sticks', callback_data='sticks')],
            [InlineKeyboardButton('Beverages', callback_data='beverages')]
        ]

        update.message.reply_text(user_text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif CART.lower() in user_text:
        reply_text = "this is your orders: "
        for data in context.user_data['cart']:
            reply_text = reply_text + data + ", "
        keyboard = [
            [InlineKeyboardButton('Clear', callback_data='clear'),
             InlineKeyboardButton('Place Order', callback_data='placeOrder')]
        ]
        update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif update.message.text in PIZZAS:
        # keyboard = [
        #     [InlineKeyboardButton('Add to cart', callback_data='addToCart')]
        # ]

        # new_user_text = '<a href="https://static.toiimg.com/thumb/56933159.cms?imgsize=686279&width=800&height=800">' + user_text + '</a>'
        # update.message.reply_text(new_user_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.HTML)
        pass
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



