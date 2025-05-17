from aiogram import Router
from aiogram import Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
import requests
from utils.config import Config
import os
from datetime import datetime
from utils.keyboard import commands_kb, get_saves_kb
from utils.utils import Times, get_minutes, to_hours
from utils.utils import get_saves

config = Config('config/config.json')
router = Router()

@router.message(Command('get'))
async def get_data(msg: Message, bot: Bot):
    name = datetime.now().date().strftime(r'%Y-%m-%d')
    requests.get(
        f'{config.url}/save-temp-data',
        json={'name': name},
        headers=config.headers
        )

    learn_time = Times()
    code_time = Times()

    learn_time.minutes = get_minutes(
        name='learn', 
        path=f'../server/temp/{name}.json'
        )
    code_time.minutes = get_minutes(
        name='code', 
        path=f'../server/temp/{name}.json'
        )
    to_hours(learn_time)
    to_hours(code_time)

    caption = f'''
CODE TIME: {code_time.hours} hours {code_time.minutes} minute
LEARN TIME: {learn_time.hours} hours {learn_time.minutes} minute'''

    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{name}.jpg'),
        caption=caption,
        reply_markup=commands_kb
        )

@router.message(Command('hui'))
async def hui(msg: Message):
    # print(get_saves_kb())
    await msg.answer('hui', reply_markup=get_saves_kb())

@router.callback_query()
async def saves_cb(cb: CallbackQuery, bot: Bot):
    saves = get_saves('../server/saves')
    if cb.data.split('_')[0] == 'Next':
        await cb.answer()
        page = int(cb.data.split('_')[1]) + 1
        await cb.message.answer('hui', reply_markup=get_saves_kb(page))

    if cb.data.split('_')[0] == 'Previous':
        page = int(cb.data.split('_')[1]) - 1 
        if page >= 0:
            await cb.message.answer('hui', reply_markup=get_saves_kb(page))

    if cb.data in saves:
        await cb.answer()

        learn_time = Times()
        code_time = Times()

        learn_time.minutes = get_minutes(
            name='learn',
            path=f'../server/saves/{cb.data}/{cb.data}.json'
            )
        code_time.minutes = get_minutes(
            name='code',
            path=f'../server/saves/{cb.data}/{cb.data}.json'
            )
        to_hours(learn_time)
        to_hours(code_time)

        caption = f'''
    CODE TIME: {code_time.hours} hours {code_time.minutes} minute
    LEARN TIME: {learn_time.hours} hours {learn_time.minutes} minute'''

        await bot.send_photo(
            cb.message.chat.id,
            FSInputFile(f'../server/saves/{cb.data}/{cb.data}.jpg'),
            caption=caption,
            reply_markup=commands_kb
        )
