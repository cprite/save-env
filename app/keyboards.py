from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


async def start():
    menu_keyboard = InlineKeyboardBuilder()
    menu_keyboard.add(InlineKeyboardButton(text='Старт', callback_data='start'))

    return menu_keyboard.as_markup()


async def stop():
    menu_keyboard = InlineKeyboardBuilder()
    menu_keyboard.add(InlineKeyboardButton(text='Стоп', callback_data='stop'))

    return menu_keyboard.as_markup()
