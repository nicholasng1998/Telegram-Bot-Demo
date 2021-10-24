from telegram import Message
from telegram.ext import MessageFilter
from bot import constant


class InlineButtonFilter(MessageFilter):
    def filter(self, message: Message) -> bool:
        print(message)
        return message.text in constant.INLINE_KEYBOARDS

