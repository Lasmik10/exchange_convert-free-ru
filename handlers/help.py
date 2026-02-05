from aiogram import Router, types
from aiogram.filters import Command

router = Router()
#----------------------------------------

@router.message(Command("help"))
async def start_bot(message: types.Message):
    await message.answer((
        "Для расчета курса введите сообщение в формате:\n"
        "<число> <что> <во что>\n\n"
        "пример:\n"
        "100 USD EUR\n"
    ))