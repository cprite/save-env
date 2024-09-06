from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Bot

import asyncio
import os

import app.keyboards as kb

router = Router()
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))


@router.message(CommandStart())
async def start(message: Message):

    if message.from_user.id == 1132338630:

        await message.answer("Меню", reply_markup=await kb.start())
