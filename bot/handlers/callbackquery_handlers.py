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


def add_cart(update, context):
    add_to_cart_prefix = "addToCart."
    logging.info("User: add to cart")

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        chat_id = update.effective_user.id

        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    callback_data = update.callback_query.data
    logging.info("DEBUGGER: callback data {}".format(callback_data))
    user_query = str(callback_data).replace(add_to_cart_prefix, "")
    product_id = ""
    product_size = ""

    try:
        product_id, product_size = user_query.split(" ")
    except Exception:
        logging.info("DEBUGGER: fail to split user query into product id and size.")
        chat_id = update.effective_user.id

        reply_text = constant.COMMON_ERROR_MESSAGE
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    logging.info("DEBUGGER: client add item {} {} to cart".format(product_id, product_size))

    product_menu = constant.PRODUCT_MENU
    products = list(filter(lambda product_menu: product_menu["id"] == product_id, product_menu))

    if len(products) == 0:
        logging.info("DEBUGGER: no products with id {} found for query.".format(product_id))
        return

    product = products[0]

    order = {
        "id": len(context.user_data[constant.CART_ARRAY]) + 1,
        "name": product.get("name"),
        "size": product_size,
        "price": product.get("{}Price".format(product_size))
    }

    context.user_data[constant.CART_ARRAY].append(order)
    logging.info("DEBUGGER: Added to cart successfully.")
    context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Added to cart")


def place_order(update, context):
    logging.info("User: wanna place order.")

    if len(context.user_data[constant.CART_ARRAY]) == 0:
        logging.info("DEBUGGER: cart is empty.")
        reply_text = "Your cart is empty. Add more item to cart now."
        logging.info("Bot: {}".format(reply_text))
        update.callback_query.message.reply_text(reply_text)
        return

    context.user_data[constant.ADDRESS_REQUIRED] = True
    update.callback_query.message.reply_text('Please write your mailing address.')


def retype_address(update, context):
    logging.info("User: retype mailing address.")
    place_order(update, context)


def confirm_address(update, context):
    callback_data = update.callback_query.data
    logging.info("DEBUGGER: callback data is {}".format(callback_data))

    address = str(callback_data).replace("confirmAddress.", "")
    logging.info("DEBUGGER: client address is {}".format(address))

    context.user_data[constant.USER_ADDRESS] = address
    reply_text = 'Select a Payment Method:'
    keyboard = [
        [InlineKeyboardButton('Cash to the courier', callback_data='cashToCourier')]
    ]
    context.user_data[constant.ADDRESS_REQUIRED] = False
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text,
                             reply_markup=InlineKeyboardMarkup(keyboard))


def cash_to_courier(update, context):
    context.user_data[constant.PAYMENT_METHOD] = constant.CASH_TO_COURIER
    context.user_data[constant.COMMENT_REQUIRED] = True
    reply_text = 'Please write a comment to the order: \nFor example, an additional telephone number for contacting.'
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text)


def cancel_order(update, context):
    reply_text = 'order cancelled'
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text)


def accept_order(update, context):
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


# Iterating over every two elements in a list
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def remove_item(update, context):
    logging.info("User: want to remove item from cart")
    callback_data = update.callback_query.data
    logging.info("DEBUGGER: callback data is {}".format(callback_data))

    if constant.CART_ARRAY not in context.user_data:
        logging.info("DEBUGGER: cart is not in context user data")
        reply_text = "Your previous session has ended. Please type /start to restart the session. Thank you~"
        logging.info("Bot: " + reply_text)
        update.message.reply_text(reply_text)
        return

    reply_text = "Please select Item ID that you want to remove."
    order_ids = [order.get("id") for order in context.user_data[constant.CART_ARRAY]]

    keyboard = []
    for order_id1, order_id2 in pairwise(order_ids):
        keyboard.append([InlineKeyboardButton('Item ID: {}'.format(order_id1),
                                              callback_data='removeById.{}'.format(order_id1)),
                         InlineKeyboardButton('Item ID: {}'.format(order_id2),
                                              callback_data='removeById.{}'.format(order_id2))])
    if len(order_ids) % 2 != 0:
        keyboard.append([InlineKeyboardButton('Item ID: {}'.format(order_ids[-1]),
                                              callback_data='removeById.{}'.format(order_ids[-1]))])

    logging.info("Bot: " + reply_text)
    update.callback_query.message.reply_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


def remove_item_by_id(update, context):
    callback_data = update.callback_query.data
    logging.info("DEBUGGER: callback data is {}".format(callback_data))

    if callback_data is None:
        logging.info("DEBUGGER: callback data is None.")
        chat_id = update.effective_user.id

        reply_text = constant.COMMON_ERROR_MESSAGE
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    chosen_id = str(callback_data).replace("removeById.", "")
    logging.info("User: chosen id {}".format(chosen_id))

    orders = context.user_data[constant.CART_ARRAY]
    updated_orders = [order for order in orders if not (chosen_id == str(order.get("id")))]

    # updates cart
    context.user_data[constant.CART_ARRAY] = updated_orders

    if len(context.user_data[constant.CART_ARRAY]) == 0:
        logging.info("DEBUGGER: cart is empty.")
        reply_text = "Your cart is empty. Add more item to cart now."
        logging.info("Bot: {}".format(reply_text))
        update.callback_query.message.reply_text(reply_text)
        return

    reply_text = "Removed Item ID: {} \n"\
                 "Your updated order are listed below: \n".format(chosen_id)
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

    keyboard = [
        [InlineKeyboardButton('Remove Item', callback_data='removeItem'),
         InlineKeyboardButton('Place Order', callback_data='placeOrder')]
    ]

    update.callback_query.message.reply_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard))

