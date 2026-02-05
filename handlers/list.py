from aiogram import Router, types
from aiogram.filters import Command

from services.Frankfurter import Frankfurter

router = Router()
#----------------------------------------


@router.message(Command("list"))
async def list(message: types.Message):
    result = await Frankfurter.get_currency_list()

    await message.answer((f"{result}"))