from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Bot

import asyncio
import os

import app.keyboards as kb

from app.crawler.scraper import start_scan
from app.crawler.check import check_keys


router = Router()
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

global loop
loop = False


@router.message(CommandStart())
async def start(message: Message):
    global loop
    loop = False

    if message.from_user.id == 1132338630:

        await message.answer("Меню", reply_markup=await kb.start())

    else:
        if loop:

            while loop:

                found, compromised = await start_scan()

                try:
                    await message.edit_text(f"Общие результаты с начала работы:\n\nПроверенно ключей: {found}\nКомпроментировано ключей: {compromised}")
                except:
                    await message.answer(f"Общие результаты с начала работы:\n\nПроверенно ключей: {found}\nКомпроментировано ключей: {compromised}")

                asyncio.sleep(3600)


@router.callback_query('start')
async def start_callback(callback: CallbackQuery):
    global loop
    loop = True

    while loop:

        found, compromised = await start_scan()

        await callback.message.edit_text(f"""
                    Результаты с начала работы:\n\nПроверенно ключей: {found}\nКомпроментировано ключей: {compromised}""", reply_markup=await kb.stop())

        asyncio.sleep(3600)


@router.callback_query('stop')
async def stop_callback(callback: CallbackQuery):
    global loop
    loop = False

    await callback.message.edit_text("Работа остановлена")
    await callback.message.answer("Меню", reply_markup=await kb.start())
