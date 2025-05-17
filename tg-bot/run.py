from aiogram import Bot, Dispatcher
from utils.routers import router
from utils.config import Config
from dotenv import load_dotenv
import asyncio

load_dotenv()
config = Config('config/config.json')
bot = Bot(config.bot_token)
dp = Dispatcher()


async def run():
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
