from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode
)

PIZZAS = [
    'Buffalo Chicken Mac N Cheese (L)',
    'Ragin Pepperoni (L)',
    'Mac n Cheese (L)'
]

SODA = [
    'Coca-Cola, 2L',
    'Sprite, 2L'
]


def inline_query(update, context):

    # user query
    print(update)
    query = update.inline_query.query

    print(query)

    if query is None or query == '':
        return

    results = []

    if query == 'Large':
        for pizza in PIZZAS:
            new_user_text = '<a href="https://static.toiimg.com/thumb/56933159.cms?imgsize=686279&width=800&height=800">' + pizza + '</a>' + '$5.00'
            keyboard = [
                [InlineKeyboardButton('Add Cart', callback_data='addToCart:' + pizza)]
            ]
            results.append(InlineQueryResultArticle(
                id=pizza.upper(),
                title=pizza,
                input_message_content=InputTextMessageContent(new_user_text, parse_mode=ParseMode.HTML),
                reply_markup=InlineKeyboardMarkup(keyboard),
                description="$5.00",
                thumb_url='https://static.toiimg.com/thumb/56933159.cms?imgsize=686279&width=800&height=800'
            ))

        context.bot.answer_inline_query(update.inline_query.id, results)

    if query == 'soda beverage':
        for soda in SODA:
            new_user_text = '<a href="https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/diet-soda-good-or-bad-1296x728-feature.jpg?h=1528">' + soda + '</a>' + '$5.00'
            keyboard = [
                [InlineKeyboardButton('Add Cart', callback_data='addToCart:' + soda)]
            ]
            results.append(InlineQueryResultArticle(
                id=soda.upper(),
                title=soda,
                input_message_content=InputTextMessageContent(new_user_text, parse_mode=ParseMode.HTML),
                reply_markup=InlineKeyboardMarkup(keyboard),
                description="$2.99",
                thumb_url='https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/diet-soda-good-or-bad-1296x728-feature.jpg?h=1528'
            ))

        context.bot.answer_inline_query(update.inline_query.id, results)