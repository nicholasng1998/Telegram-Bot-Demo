from bot import constant


def init(context):
    context.user_data[constant.CART_ARRAY] = []
    context.user_data[constant.ADDRESS_REQUIRED] = False
    context.user_data[constant.COMMENT_REQUIRED] = False
