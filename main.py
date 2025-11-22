import logging
import asyncio

from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from handlers import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())

    except Exception as e:
        print(e)