from aiogram import Bot, Dispatcher
import requests
from aiogram.filters import Command
from aiogram.types import message, FSInputFile
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import asyncio
import json
import os

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command('get'))
async def get(msg : message):
    requests.post(
        'http://127.0.0.1:5000/get-data',
        json={'name': datetime.now().date().strftime(r'%Y-%m-%d')}
        )
    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{datetime.now().date()}.jpg'))
    os.remove(f'../server/temp/{datetime.now().date()}.jpg')
    os.remove(f'../server/temp/{datetime.now().date()}.json')


async def run():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
