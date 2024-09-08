from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Bot

import asyncio
import datetime

import app.keyboards as kb

from app.crawler.scanner import start_scan
from app.crawler.statistics import get_stat


router = Router()

global loop
loop = False


@router.message(CommandStart())
async def start(message: Message):

    if message.from_user.id == 1132338630:

        await message.answer("Menu", reply_markup=await kb.start())

    else:

        scan_time, total_found, last_found, total_compromised, last_compromised = get_stat()

        try:
            await message.edit_text(f"Scan results:\n\n- <b>Total keys checked:</b> {total_found}\n- <b>New keys checked:</b> {last_found}\n\n- <b>Total compromised keys:</b> {total_compromised}\n- <b>New compromised keys:</b> {last_compromised}\n\n<i>Last scan: {scan_time}</i>", parse_mode="HTML")
        except:
            await message.answer(f"Scan results:\n\n- <b>Total keys checked:</b> {total_found}\n- <b>New keys checked:</b> {last_found}\n\n- <b>Total compromised keys:</b> {total_compromised}\n- <b>New compromised keys:</b> {last_compromised}\n\n<i>Last scan: {scan_time}</i>", parse_mode="HTML")

        await asyncio.sleep(60)


@router.callback_query(F.data == "start")
async def start_callback(callback: CallbackQuery):
    global loop
    loop = True

    while loop:

        start_scan()

        scan_time, total_found, last_found, total_compromised, last_compromised = get_stat()

        await callback.message.answer(f"Scan results:\n\n- <b>Total keys checked:</b> {total_found}\n- <b>New keys checked:</b> {last_found}\n\n- <b>Total compromised keys:</b> {total_compromised}\n- <b>New compromised keys:</b> {last_compromised}\n\n<i>Last scan: {scan_time}</i>", reply_markup=await kb.stop(), parse_mode="HTML")

        await asyncio.sleep(3600)


@router.callback_query(F.data == "stop")
async def stop_callback(callback: CallbackQuery):
    global loop
    loop = False

    await callback.message.edit_text("Работа остановлена")
    await callback.message.answer("Menu", reply_markup=await kb.start())
