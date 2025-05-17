from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardButton, InlineKeyboardMarkup
    )
from utils.utils import get_saves

commands_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/get', callback_data='/get')],
    [KeyboardButton(text='/history', callback_data='/history')]
    ],
    resize_keyboard=True)

def get_saves_kb(page=1):
    saves = get_saves('../server/saves')
    items_per_page = 2
    start = (page - 1) * items_per_page
    end = start + items_per_page
    sliced_saves = saves[start:end]

    page_kb =[[
        InlineKeyboardButton(text=i, callback_data=i)] 
        for i in sliced_saves
        ]
    page_kb.append([
        InlineKeyboardButton(text='Previous', callback_data=f'Previous_{page}'),
        InlineKeyboardButton(text='Next', callback_data=f'Next_{page}'),
    ])

    return InlineKeyboardMarkup(inline_keyboard=page_kb)
 