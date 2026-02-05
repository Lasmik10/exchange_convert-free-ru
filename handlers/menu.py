from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Как использовать бота"),
        BotCommand(command="/list", description="Список поддерживаемых валют"),
        BotCommand(command="/convert", description="Начать конвертацию"),
    ]
    await bot.set_my_commands(commands)