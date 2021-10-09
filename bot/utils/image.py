from pathlib import Path
from telegram import InputMediaPhoto


def upload_local_photo(image: str):
    try:
        image_file = open(image, 'rb')
        image_byte = image_file.read()
        image_file.close()
        return InputMediaPhoto(image_byte)
    except IOError as e:
        print("IO exception here")
        return None
