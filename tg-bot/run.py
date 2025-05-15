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
headers = {'Authorization': getenv('HEADERS')}

@dp.message(Command('get'))
async def get(msg : message):
    requests.get(
        'http://127.0.0.1:5000/save-temp-data',
        json={'name': datetime.now().date().strftime(r'%Y-%m-%d')},
        headers=headers
        )
    
    with open(f'../server/temp/{datetime.now().date()}.json') as f:
        data = json.load(f)

    learn_time = {'hours':0, 'minute': 0}
    code_time = {'hours':0, 'minute': 0}
    for i in data:
        print()
        if i.split('_')[0] == 'learn':
            learn_time['minute'] += data[i]
            print(learn_time)
        elif i.split('_')[0] == 'code':
            code_time['minute'] += data[i]
            print(code_time)

    print(learn_time, code_time)

    while learn_time['minute'] > 60: 
        learn_time['minute'] -= 60
        learn_time['hours'] += 1
        print(learn_time)
    while code_time['minute'] > 60: 
        code_time['minute'] -= 60
        code_time['hours'] += 1
        print(code_time)

    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{datetime.now().date()}.jpg'),
        caption=f'''
CODE TIME: {code_time["hours"]} hours {code_time["minute"]} minute
LEARN TIME: {learn_time["hours"]} hours {learn_time["minute"]} minute
        '''
        )
    os.remove(f'../server/temp/{datetime.now().date()}.jpg')
    os.remove(f'../server/temp/{datetime.now().date()}.json')


async def run():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
