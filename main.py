import asyncio
import logging

from aiogram import Bot, Dispatcher

import configparser
config = configparser.ConfigParser()
config.read("config.ini")

from handlers import register_routers
from handlers.menu import set_bot_commands

logging.basicConfig(level=logging.INFO)
#----------------------------------------

async def main():
    bot = Bot(token=config['BOT']['TOKEN'])

    dp = Dispatcher()

    register_routers(dp)
    await set_bot_commands(bot)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')