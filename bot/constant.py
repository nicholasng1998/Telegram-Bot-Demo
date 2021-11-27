"""
    Emoji can be found from url below:
    https://www.iemoji.com/
"""

# KeyBoard Menu
CATALOG = "📒 Catalog"
ORDER_HISTORY = "📄 Order History"
MY_PROFILE = "👤 My Profile"
CART = "🛒 Cart"
INLINE_KEYBOARDS = [
    CATALOG,
    ORDER_HISTORY,
    MY_PROFILE,
    CART
]

# Validators & User Data
CART_ARRAY = "cartArray"
ADDRESS_REQUIRED = "addressRequired"
COMMENT_REQUIRED = "commentRequired"
USER_ADDRESS = "userAddress"
PAYMENT_METHOD = "paymentMethod"
CASH_TO_COURIER = "cashToCourier"
USER_COMMENT = "userComment"

# General
GREETING_MESSAGE = '''
Hello 👋 Welcome to Demo Bare Bear shop. 🧸🧸
Hope you are doing well today.
To start the journey, you can type /start.
To get more info, you can type /help.
📱 If you have any question, you are always welcome to pm me:
👇👇👇
https://m.me/devauto.solution
'''

HELP_MESSAGE = '''
This is a demo version of seller bot.
You can try to do an end to end flow of item ordering:
View Catalog 👉 Choose Item 👉 Add Cart 👉 Place Order
'''

# Exception
COMMAND_NOT_FOUND = "Sorry, I\'m worry that I can\'t help you on that."
COMMON_ERROR_MESSAGE = "System has error occurred. Please try again later."

# Poster file id
POSTER_FILE_ID = "AgACAgUAAxkBAAIJCGGPhXNAspCTSCR2myUwI2XQ79aGAAKkrjEbYtl4VBf4-lz0GZ2xAQADAgADbQADIgQ"
DEVAUTO_POSTER_FILE_ID = "AgACAgUAAxkBAAMGYaJmnQglW2tM9m5fYYUAAVIHSijfAAJ3rjEbv4kYVZBQh53flMDzAQADAgADbQADIgQ"

# Product Menu
# PRODUCT_MENU = [
#     # standing
#     {
#         "id": "standingGrizzly",
#         "name": "Standing Grizzly",
#         "type": "grizzly",
#         "pose": "standing",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Standing Grizzly",
#         "photoFileId": "AgACAgUAAxkBAAIE2GF0NucgX2jhUJ16GW05e8G06d7WAAJxrTEbi6SgV-yz9qdts-7UAQADAgADcwADIQQ"
#     },
#     {
#         "id": "standingIceBear",
#         "name": "Standing Ice Bear",
#         "type": "icebear",
#         "pose": "standing",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Standing Ice Bear",
#         "photoFileId": "AgACAgUAAxkBAAIE2WF0Nv72teAH9ksfqlPFMBw_0t-hAAJzrTEbi6SgVwuoCP-J84-_AQADAgADcwADIQQ"
#     },
#     {
#         "id": "standingBear",
#         "name": "Standing Panda",
#         "type": "panda",
#         "pose": "standing",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Standing Panda",
#         "photoFileId": "AgACAgUAAxkBAAIE2mF0NxBRHPI6pL1B-0IAAYEZafn_XQACdK0xG4ukoFc-rAyoJMU9ZQEAAwIAA3MAAyEE"
#     },
#     # sleeping
#     {
#         "id": "sleepingGrizzly",
#         "name": "Sleeping Grizzly",
#         "type": "grizzly",
#         "pose": "sleeping",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Sleeping Grizzly",
#         "photoFileId": "AgACAgUAAxkBAAIE22F0Nzoc7TRniDVtbb-VRHjDiTAaAAJ1rTEbi6SgV6old2lNMFqZAQADAgADcwADIQQ"
#     },
#     {
#         "id": "sleepingIceBear",
#         "name": "Sleeping Ice Bear",
#         "type": "icebear",
#         "pose": "sleeping",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Sleeping Ice Bear",
#         "photoFileId": "AgACAgUAAxkBAAIE3GF0N2C1oUa3fnzAEaJgSvLLUv4aAAJ2rTEbi6SgVycIufVA0QEOAQADAgADcwADIQQ"
#     },
#     {
#         "id": "sleepingPanda",
#         "name": "Sleeping Panda",
#         "type": "panda",
#         "pose": "sleeping",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Sleeping Panda",
#         "photoFileId": "AgACAgUAAxkBAAIE3WF0N3CA7-coOPMq3sepjnC_Udx4AAJ3rTEbi6SgVxsypXSYZaw5AQADAgADcwADIQQ"
#     },
#     # crawling
# {
#         "id": "crawlingGrizzly",
#         "name": "Crawling Grizzly",
#         "type": "grizzly",
#         "pose": "crawling",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Crawling Grizzly",
#         "photoFileId": "AgACAgUAAxkBAAIExmF0M1OBP1gQd7P8XuGZFyMFKp_cAAJrrTEbi6SgV4l0NBXZG1bIAQADAgADcwADIQQ"
#     },
#     {
#         "id": "crawlingIceBear",
#         "name": "Crawling Ice Bear",
#         "type": "icebear",
#         "pose": "crawling",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Crawling Ice Bear",
#         "photoFileId": "AgACAgUAAxkBAAIE3mF0N48blP0iMIAkXV71rRUm4mZHAAJ4rTEbi6SgV-rDw0O9xQaLAQADAgADcwADIQQ"
#     },
#     {
#         "id": "crawlingPanda",
#         "name": "Crawling Panda",
#         "type": "panda",
#         "pose": "crawling",
#         "50cmPrice": 35.00,
#         "40cmPrice": 27.00,
#         "30cmPrice": 25.00,
#         "25cmPrice": 8.00,
#         "description": "Crawling Panda",
#         "photoFileId": "AgACAgUAAxkBAAIE32F0N6M70ZKhTR3jaa1LgWSmStOfAAJ5rTEbi6SgV2RNV9fCH_0KAQADAgADcwADIQQ"
#     }
# ]

DEVAUTO_PRODUCT_MENU = [
    # standing
    {
        "id": "standingGrizzly",
        "name": "Standing Grizzly",
        "type": "grizzly",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Grizzly",
        "photoFileId": "AgACAgUAAxkBAAMHYaJnGlLcbvZq35CCBanFIb1yHIsAAvKvMRudnhFV-DSPCKrQAAF0AQADAgADbQADIgQ"
    },
    {
        "id": "standingIceBear",
        "name": "Standing Ice Bear",
        "type": "icebear",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAMIYaJnHT4eR8t7GCR8E0djvCyT_wIAAvOvMRudnhFVPQ9i7Bsc89UBAAMCAANtAAMiBA"
    },
    {
        "id": "standingBear",
        "name": "Standing Panda",
        "type": "panda",
        "pose": "standing",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Standing Panda",
        "photoFileId": "AgACAgUAAxkBAAMJYaJnIGLq_uZxOeBgJvga8800gosAAvSvMRudnhFVBm0iUm-n6hYBAAMCAANtAAMiBA"
    },
    # sleeping
    {
        "id": "sleepingGrizzly",
        "name": "Sleeping Grizzly",
        "type": "grizzly",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Grizzly",
        "photoFileId": "AgACAgUAAxkBAAMNYaJncq-1rcEwFOkjMdMbKX1h_y4AAvWvMRudnhFV2rsK_ZXptZsBAAMCAANzAAMiBA"
    },
    {
        "id": "sleepingIceBear",
        "name": "Sleeping Ice Bear",
        "type": "icebear",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAMOYaJndcCJH7cdB55aXodSpduGvhEAAvevMRudnhFVseEQ9B7Fw-IBAAMCAANzAAMiBA"
    },
    {
        "id": "sleepingPanda",
        "name": "Sleeping Panda",
        "type": "panda",
        "pose": "sleeping",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Sleeping Panda",
        "photoFileId": "AgACAgUAAxkBAAMPYaJneAzsLP7YxFka_1kj58JS-3kAAvavMRudnhFVfnJHblT1yCkBAAMCAANzAAMiBA"
    },
    # crawling
{
        "id": "crawlingGrizzly",
        "name": "Crawling Grizzly",
        "type": "grizzly",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Grizzly",
        "photoFileId": "AgACAgUAAxkBAAMQYaJnlvmG194VcUwJ9QLM_DlTr3YAAvivMRudnhFVAv_0MBukAAEhAQADAgADcwADIgQ"
    },
    {
        "id": "crawlingIceBear",
        "name": "Crawling Ice Bear",
        "type": "icebear",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Ice Bear",
        "photoFileId": "AgACAgUAAxkBAAMRYaJnmNnEPVqYuhullzke3rqLx-QAAvmvMRudnhFVc8-7ynnFdpABAAMCAANzAAMiBA"
    },
    {
        "id": "crawlingPanda",
        "name": "Crawling Panda",
        "type": "panda",
        "pose": "crawling",
        "50cmPrice": 35.00,
        "40cmPrice": 27.00,
        "30cmPrice": 25.00,
        "25cmPrice": 8.00,
        "description": "Crawling Panda",
        "photoFileId": "AgACAgUAAxkBAAMSYaJnnFL29dp2K_8etLh13albrP8AAvqvMRudnhFVYaAeK6hlC-YBAAMCAANzAAMiBA"
    }
]
