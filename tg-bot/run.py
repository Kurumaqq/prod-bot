from aiogram import Bot, Dispatcher
import requests
from aiogram.filters import Command
from aiogram.types import message, FSInputFile
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import asyncio
from utils.routers import router
import json
import os

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()


async def run():
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
