from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineQueryResultDocument,
    InlineQueryResultPhoto,
    InlineQueryResultCachedPhoto,
InlineQueryResultCachedDocument,
    InlineKeyboardButton,
    ParseMode
)
from bot import constant
from bot.config import LOGGING_FORMAT
import logging
import os

# PIZZAS = [
#     'Buffalo Chicken Mac N Cheese (L)',
#     'Ragin Pepperoni (L)',
#     'Mac n Cheese (L)'
# ]
#
# SODA = [
#     'Coca-Cola, 2L',
#     'Sprite, 2L'
# ]

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


# def inline_query(update, context):
#
#     # user query
#     query = update.inline_query.query
#
#     if query is None or query == '':
#         logging.info("DEBUGGER: user inline query is blank.")
#         return
#
#     results = []
#
#     if query == 'Large':
#         for pizza in PIZZAS:
#             new_user_text = '<a href="https://static.toiimg.com/thumb/56933159.cms?imgsize=686279&width=800&height=800">' + pizza + '</a>' + '$5.00'
#             keyboard = [
#                 [InlineKeyboardButton('Add Cart', callback_data='addToCart:' + pizza)]
#             ]
#             results.append(InlineQueryResultArticle(
#                 id=pizza.upper(),
#                 title=pizza,
#                 input_message_content=InputTextMessageContent(new_user_text, parse_mode=ParseMode.HTML),
#                 reply_markup=InlineKeyboardMarkup(keyboard),
#                 description="$5.00",
#                 thumb_url='https://static.toiimg.com/thumb/56933159.cms?imgsize=686279&width=800&height=800'
#             ))
#
#         context.bot.answer_inline_query(update.inline_query.id, results)
#
#     if query == 'soda beverage':
#         for soda in SODA:
#             new_user_text = '<a href="https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/diet-soda-good-or-bad-1296x728-feature.jpg?h=1528">' + soda + '</a>' + '$5.00'
#             keyboard = [
#                 [InlineKeyboardButton('Add Cart', callback_data='addToCart:' + soda)]
#             ]
#             results.append(InlineQueryResultArticle(
#                 id=soda.upper(),
#                 title=soda,
#                 input_message_content=InputTextMessageContent(new_user_text, parse_mode=ParseMode.HTML),
#                 reply_markup=InlineKeyboardMarkup(keyboard),
#                 description="$2.99",
#                 thumb_url='https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/diet-soda-good-or-bad-1296x728-feature.jpg?h=1528'
#             ))
#
#         context.bot.answer_inline_query(update.inline_query.id, results)

def inline_query(update, context):
    # user query
    query = str(update.inline_query.query)

    if query is None or query == '':
        logging.info("DEBUGGER: user inline query is blank.")
        return

    user_query = query.lower()
    product_type = ""
    product_size = ""

    try:
        product_type, product_size = user_query.split(" ")
    except Exception:
        logging.info("DEBUGGER: fail to split user query into type and size.")
        chat_id = update.effective_user.id

        reply_text = constant.COMMON_ERROR_MESSAGE
        logging.info("Bot: " + reply_text)
        update.callback_query.bot.send_message(chat_id=chat_id, text=reply_text)
        return

    product_menu = constant.PRODUCT_MENU
    products = list(filter(lambda product_menu: product_menu['type'] == product_type, product_menu))

    if len(products) == 0:
        logging.info("DEBUGGER: no products found for query: " + product_type)
        return

    results = []
    for product in products:
        keyboard = [
            [InlineKeyboardButton('🛒 Add To Cart', callback_data=product.get("name"))]
        ]

        caption = "Product Name: {} \n" \
                  "Size: {} \n" \
                  "Price: RM {} \n" \
                  "Description: {} \n"\
            .format(product.get("name"),
                    product_size,
                    product.get("{}Price".format(product_size)),
                    product.get("description"))

        inline_query_result = InlineQueryResultCachedPhoto(
            id=product.get("name"),
            title=product.get("name"),
            photo_file_id=product.get("photoFileId"),
            description=product.get("description"),
            caption=caption,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        results.append(inline_query_result)

    context.bot.answer_inline_query(update.inline_query.id, results)
