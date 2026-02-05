from aiogram import Router, types
from aiogram.filters import Command

router = Router()
#----------------------------------------

@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer((
        "👋 Привет! Я помогу отслеживать курсы валют."
        "Для начала работы нажмите кнопку \"Меню\" 👇"
    ))