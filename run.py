import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router # обработка запросов через роутер


load_dotenv()
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot, polling_timeout = 900)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
