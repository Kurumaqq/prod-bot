from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import asyncio
import json

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

async def run():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
