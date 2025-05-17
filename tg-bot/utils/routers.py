from aiogram import Router
from aiogram import Bot
from aiogram.types import message, FSInputFile
from aiogram.filters import Command
import requests
import json
from utils.config import Config
import os
from datetime import datetime
from utils.keyboard import commands
from utils.utils import Times, get_minutes, to_hours

config = Config('config/config.json')
router = Router()

@router.message(Command('get'))
async def get_data(msg: message, bot: Bot):
    requests.get(
        f'{config.url}/save-temp-data',
        json={'name': datetime.now().date().strftime(r'%Y-%m-%d')},
        headers=config.headers
        )

    learn_time = Times()
    code_time = Times()

    learn_time.minutes = get_minutes('learn')
    code_time.minutes = get_minutes('code')
    learn_time.hours = to_hours(learn_time.minutes)
    code_time.hours = to_hours(code_time.minutes)

    caption = f'''
CODE TIME: {code_time.hours} hours {code_time.minutes} minute
LEARN TIME: {learn_time.hours} hours {learn_time.minutes} minute'''

    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{datetime.now().date()}.jpg'),
        caption=caption,
        reply_markup=commands
        )
    os.remove(f'../server/temp/{datetime.now().date()}.jpg')
    os.remove(f'../server/temp/{datetime.now().date()}.json')
