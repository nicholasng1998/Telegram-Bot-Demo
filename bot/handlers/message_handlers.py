import logging
import sqlite3
from bot import sql_constant
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode
)
from bot import constant
from bot.config import LOGGING_FORMAT

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def handle(update, context):

    user_text = update.message.text
    logging.info("User: " + user_text)

    # catalog button pressed
    if constant.CATALOG == user_text:
        catalog_button_response(update, context)

    # cart button pressed
    elif constant.CART == user_text:
        cart_button_response(update, context)

    # my profile button pressed
    elif constant.MY_PROFILE == user_text:
        # TODO
        chat_id = update.message.chat.id
        con = sqlite3.connect("bot_data.db")
        cursor_obj = con.cursor()
        cursor_obj.execute(sql_constant.SELECT_USER.format(chat_id))
        users = cursor_obj.fetchall()
        if len(users) > 0:
            user_id, name, address, chat_id = users[0]
            logging.info("User chat id: {}".format(str(chat_id)))
            my_profile_format = "Name: {} \n".format(name)
            if address is not None:
                my_profile_format = my_profile_format + "Address {} \n".format(address)
                keyboard = [
                    [InlineKeyboardButton('Edit Address', callback_data='editAddress')]
                ]
                update.message.reply_text(text=my_profile_format, reply_markup=InlineKeyboardMarkup(keyboard),
                                          parse_mode=ParseMode.HTML)
            elif address is None:
                keyboard = [
                    [InlineKeyboardButton('Add Address', callback_data='addAddress')]
                ]
                update.message.reply_text(text=my_profile_format, reply_markup=InlineKeyboardMarkup(keyboard),
                                          parse_mode=ParseMode.HTML)

        elif len(users) == 0:
            reply_text = constant.COMMON_ERROR_MESSAGE
            logging.info("Bot: " + reply_text)
            update.message.reply_text(reply_text, parse_mode=ParseMode.HTML)
        con.close()

    # order history button pressed
    elif constant.ORDER_HISTORY == user_text:
        # TODO
        return

    elif constant.ADDRESS_REQUIRED in context.user_data and context.user_data[constant.ADDRESS_REQUIRED]:
        logging.info("DEBUGGER: user entered order mailing address")
        reply_text = 'Your address is: \n' \
                     '{}'.format(user_text)
        keyboard = [
            [InlineKeyboardButton('Retype', callback_data='retype'),
             InlineKeyboardButton('Confirm', callback_data='confirmAddress.{}'.format(user_text))]
        ]
        update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif constant.COMMENT_REQUIRED in context.user_data and context.user_data[constant.COMMENT_REQUIRED]:
        logging.info("DEBUGGER: user entered order comment")
        context.user_data[constant.USER_COMMENT] = user_text
        generate_summary(update, context)

    else:
        logging.info("DEBUGGER: Enter else statement")
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
        [InlineKeyboardButton('Remove Item', callback_data='removeItem'),
         InlineKeyboardButton('Place Order', callback_data='placeOrder')]
    ]

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.message.reply_text(reply_text)
        return

    if len(context.user_data[constant.CART_ARRAY]) == 0:
        logging.info("DEBUGGER: cart is empty.")
        reply_text = "Your cart is empty. Add more item to cart now."
        logging.info("Bot: {}".format(reply_text))
        update.message.reply_text(reply_text)
        return

    reply_text = "Your order are listed below: \n"
    logging.info("DEBUGGER: Number of orders: " + str(len(context.user_data[constant.CART_ARRAY])))
    order_text_format = "\nItem ID: {} \n" \
                        "Item Name: {} {}\n" \
                        "Price: {}\n"
    total_price = 0
    for order in context.user_data[constant.CART_ARRAY]:
        reply_text += order_text_format.format(str(order.get("id")), order.get("name"),
                                               order.get("size"), order.get("price"))
        total_price += float(order.get("price"))

    reply_text += "\n\nTotal: RM {}".format(total_price)
    logging.info("Bot: " + reply_text)
    update.message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def generate_summary(update, context):
    logging.info("DEBUGGER: Generate order summary.")

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.message.reply_text(reply_text)
        return

    if len(context.user_data[constant.CART_ARRAY]) == 0:
        logging.info("DEBUGGER: cart is empty.")
        reply_text = "Your cart is empty. Add more item to cart now."
        logging.info("Bot: {}".format(reply_text))
        update.message.reply_text(reply_text)
        return

    reply_text = "Your order are listed below: \n"
    logging.info("DEBUGGER: Number of orders: " + str(len(context.user_data[constant.CART_ARRAY])))
    order_text_format = "\nItem ID: {} \n" \
                        "Item Name: {} {}\n" \
                        "Price: {}\n"
    total_price = 0
    for order in context.user_data[constant.CART_ARRAY]:
        reply_text += order_text_format.format(str(order.get("id")), order.get("name"),
                                               order.get("size"), order.get("price"))
        total_price += float(order.get("price"))

    reply_text += "\n\nTotal: RM {}".format(total_price)
    reply_text += "\nAddress: {}" \
                  "\nPayment Method: {}" \
                  "\nComment: {}".format(context.user_data[constant.USER_ADDRESS],
                                         context.user_data[constant.PAYMENT_METHOD],
                                         context.user_data[constant.USER_COMMENT])

    keyboard = [
        [InlineKeyboardButton('Cancel', callback_data='cancelOrder'),
         InlineKeyboardButton('Accept', callback_data='acceptOrder')]
    ]
    context.user_data[constant.COMMENT_REQUIRED] = False
    update.message.reply_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.HTML)
