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
    date = datetime.now().date().strftime(r'%Y-%m-%d')
    requests.post(
        f'{config.url}/save/temp',
        headers=config.headers,
        params={'date': date},
        )

    learn_time = Times()
    code_time = Times()
    path = '../server/temp'

    get_time(
        name='learn', 
        path=f'{path}/{date}.json',
        time=learn_time
        )
    get_time(
        name='code', 
        path=f'{path}/{date}.json',
        time=code_time
        )

    await bot.send_photo(msg.chat.id,
        FSInputFile(f'../server/temp/{date}.jpg'),
        caption=get_caption(code_time, learn_time),
        reply_markup=commands_kb
        )
    
    os.remove(f'../server/temp/{date}.jpg')
    os.remove(f'../server/temp/{date}.json')

@router.message(Command('history'))
async def history(msg: Message):
    await msg.answer('Your actives history', reply_markup=get_saves_kb())

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
