from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

async def run():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
