from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/get', callback_data='/get')]
    ],
    resize_keyboard=True)
