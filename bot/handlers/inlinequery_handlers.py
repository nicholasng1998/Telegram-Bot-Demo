from telegram import (
    InlineKeyboardMarkup,
    InlineQueryResultCachedPhoto,
    InlineKeyboardButton,
)
from bot import constant
from bot.config import LOGGING_FORMAT
import logging

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def inline_query(update, context):
    logging.info("DEBUGGER: Enter inline query handlers.")

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
            [InlineKeyboardButton('🛒 Add To Cart', callback_data="addToCart.{} {}"
                                  .format(product.get("id"), product_size))]
        ]

        caption = "Product Name: {} \n" \
                  "Size: {} \n" \
                  "Price: RM {} \n" \
                  "Description: {} \n" \
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
