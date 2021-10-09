from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatAction
)
import time
import logging


def catalog(update, context):
    keyboard = [
        [InlineKeyboardButton('Pizza', callback_data='pizza'), InlineKeyboardButton('Sticks', callback_data='sticks')],
        [InlineKeyboardButton('Beverages', callback_data='beverages')]
    ]
    update.callback_query.message.edit_text('Catalog \nThis is the main directory',
                                            reply_markup=InlineKeyboardMarkup(keyboard))


def pizza(update, context):
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Large 14', switch_inline_query_current_chat="Large"), InlineKeyboardButton('Medium 12', switch_inline_query_current_chat='Medium')],
        [InlineKeyboardButton('Small 9', switch_inline_query_current_chat='Small')]
    ]
    update.callback_query.message.edit_text('Choose your pizza size',
                                            reply_markup=InlineKeyboardMarkup(keyboard))


def sticks(update, context):
    update.message.reply_text('sticks')


def beverages(update, context):
    keyboard = [
        [InlineKeyboardButton('Catalog', callback_data='catalog')],
        [InlineKeyboardButton('Soda', switch_inline_query_current_chat="soda beverage")]
    ]
    update.callback_query.message.edit_text('Choose your beverages',
                                            reply_markup=InlineKeyboardMarkup(keyboard))


def soda(update, context):
    update.callback_query.message.reply_text('soda')


def large(update, context):
    update.callback_query.message.reply_text('large')


def medium(update, context):
    update.message.reply_text('medium')


def small(update, context):
    update.message.reply_text('small')


def add_cart(update, context):
    context.user_data['cart'].append(update.callback_query.data)


def place_order(update, context):
    print(update)
    print(dir(update))
    print(context)
    print(dir(context))
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
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard))


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
    context.bot.send_message(chat_id=update.effective_user.id, text="Your order has been successfully delivered! Thank you for using our service. Do not forget to share with your friend.")



