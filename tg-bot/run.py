from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
from dotenv import load_dotenv
from os import getenv
import asyncio
import json

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command('get'))
def get(msg : message):
    pass


async def run():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
