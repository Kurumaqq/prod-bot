from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import Router
from aiogram import Bot
from aiogram import F
from utils.utils import Times, get_time, get_caption
from utils.utils import get_saves
from utils.keyboard import commands_kb, get_saves_kb
from utils.config import Config
from datetime import datetime
import requests
import os

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
    path = '../server/temp'

    get_time(
        name='learn', 
        path=f'{path}/{name}.json',
        time=learn_time
        )
    get_time(
        name='code', 
        path=f'{path}/{name}.json',
        time=code_time
        )

    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{name}.jpg'),
        caption=get_caption(code_time, learn_time),
        reply_markup=commands_kb
        )
    
    os.remove(f'../server/temp/{name}.jpg')
    os.remove(f'../server/temp/{name}.json')

@router.message(Command('history'))
async def hui(msg: Message):
    await msg.answer('hui', reply_markup=get_saves_kb())

@router.callback_query(F.data.startswith('Next_'))
async def next_cb(cb: CallbackQuery):
    await cb.answer()
    page = int(cb.data.split('_')[1]) + 1
    await cb.message.delete()
    await cb.message.answer('hui', reply_markup=get_saves_kb(page))

@router.callback_query(F.data.startswith('Previous_'))
async def next_cb(cb: CallbackQuery):
    await cb.answer()
    page = int(cb.data.split('_')[1]) - 1 
    if page > 0:
        await cb.message.delete()
        await cb.message.answer('hui', reply_markup=get_saves_kb(page))

@router.callback_query()
async def send_saves(cb: CallbackQuery, bot: Bot):
    await cb.answer()
    saves = get_saves('../server/saves')
    if cb.data in saves:
        learn_time = Times()
        code_time = Times()
        path = f'../server/saves/{cb.data}'

        get_time(
            name='learn',
            path=f'{path}/{cb.data}.json',
            time=learn_time
            )
        get_time(
            name='code',
            path=f'{path}/{cb.data}.json',
            time=code_time
            )
        
        await bot.send_photo(
            cb.message.chat.id,
            FSInputFile(f'../server/saves/{cb.data}/{cb.data}.jpg'),
            caption=get_caption(code_time, learn_time),
            reply_markup=commands_kb
        )
