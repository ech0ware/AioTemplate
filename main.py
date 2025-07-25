import asyncio
from aiogram import Bot, Dispatcher

from db import *

# Импорт роутеров
from app.handlers.user import user_router
from app.handlers.admin import admin_router
# from app.handlers.FILE import NAMEROUTER

from config import TOKEN
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)

# запуск
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        db_init()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершен')