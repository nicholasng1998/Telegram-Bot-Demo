"""
    Emoji can be found from url below:
    https://www.iemoji.com/
"""

# KeyBoard Menu
CATALOG = "📒 Catalog"
ORDER_HISTORY = "📄 Order History"
MY_PROFILE = "👤 My Profile"
CART = "🛒 Cart"

# Validators
CART_ARRAY = "cartArray"
ADDRESS_REQUIRED = "addressRequired"
COMMENT_REQUIRED = "commentRequired"

# General
GREETING_MESSAGE = '''
Hello 👋 Welcome to Demo Bare Bear shop. 🧸🧸
Hope you are doing well today.
To start the journey, you can type /start.
To get more info, you can type /help.
📱 If you have any question, you are always welcome to pm me:
👇👇👇
https://m.me/
'''

HELP_MESSAGE = '''
This is a demo version of seller bot.
You can try to do an end to end flow of item ordering:
View Catalog 👉 Choose Item 👉 Add Cart 👉 Place Order
'''

# Exception
COMMAND_NOT_FOUND = "Sorry, I\'m worry that I can\'t help you on that."
COMMON_ERROR_MESSAGE = "System has error occurred. Please try again later."

# Product Menu
PRODUCT_MENU = [
    # standing
    {
        "name": "Standing Grizzly",
        "type": "grizzly",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Grizzly",
        "photoFileId": "AgACAgUAAxkBAAIE2GF0NucgX2jhUJ16GW05e8G06d7WAAJxrTEbi6SgV-yz9qdts-7UAQADAgADcwADIQQ"
    },
    {
        "name": "Standing Ice Bear",
        "type": "ice bear",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAIE2WF0Nv72teAH9ksfqlPFMBw_0t-hAAJzrTEbi6SgVwuoCP-J84-_AQADAgADcwADIQQ"
    },
    {
        "name": "Standing Panda",
        "type": "panda",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Panda",
        "photoFileId": "AgACAgUAAxkBAAIE2mF0NxBRHPI6pL1B-0IAAYEZafn_XQACdK0xG4ukoFc-rAyoJMU9ZQEAAwIAA3MAAyEE"
    },
    # sleeping
    {
        "name": "Sleeping Grizzly",
        "type": "grizzly",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Grizzly",
        "photoFileId": "AgACAgUAAxkBAAIE22F0Nzoc7TRniDVtbb-VRHjDiTAaAAJ1rTEbi6SgV6old2lNMFqZAQADAgADcwADIQQ"
    },
    {
        "name": "Sleeping Ice Bear",
        "type": "ice bear",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAIE3GF0N2C1oUa3fnzAEaJgSvLLUv4aAAJ2rTEbi6SgVycIufVA0QEOAQADAgADcwADIQQ"
    },
    {
        "name": "Sleeping Panda",
        "type": "panda",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Panda",
        "photoFileId": "AgACAgUAAxkBAAIE3WF0N3CA7-coOPMq3sepjnC_Udx4AAJ3rTEbi6SgVxsypXSYZaw5AQADAgADcwADIQQ"
    },
    # crawling
{
        "name": "Crawling Grizzly",
        "type": "grizzly",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Grizzly",
        "photoFileId": "AgACAgUAAxkBAAIExmF0M1OBP1gQd7P8XuGZFyMFKp_cAAJrrTEbi6SgV4l0NBXZG1bIAQADAgADcwADIQQ"
    },
    {
        "name": "Crawling Ice Bear",
        "type": "ice bear",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAIE3mF0N48blP0iMIAkXV71rRUm4mZHAAJ4rTEbi6SgV-rDw0O9xQaLAQADAgADcwADIQQ"
    },
    {
        "name": "Crawling Panda",
        "type": "panda",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Panda",
        "photoFileId": "AgACAgUAAxkBAAIE32F0N6M70ZKhTR3jaa1LgWSmStOfAAJ5rTEbi6SgV2RNV9fCH_0KAQADAgADcwADIQQ"
    }
]
