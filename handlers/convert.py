from aiogram import Router, types
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.Frankfurter import Frankfurter

router = Router()

class ConversionStates(StatesGroup):
    waiting_for_input = State()
#----------------------------------------


@router.message(Command("convert"))
async def convert(message: types.Message, state: FSMContext):
    await message.answer((
        "Для расчета курса введите сообщение в формате:\n"
        "<число> <что> <во что>\n\n"
        "пример:\n"
        "100 USD EUR\n"
    ))
    await state.set_state(ConversionStates.waiting_for_input)
#----------------------------------------


@router.message(ConversionStates.waiting_for_input)
async def convert_request(message: types.Message, state: FSMContext):

    if message.text.count(' ') > 2:
        await message.answer("❌ Ошибка: разделите пробелами")
        await state.clear()
        return

    try:
        user_input = message.text.strip()
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Нужно ввести три значения: число, валюта1, валюта2")
        
        amount = float(parts[0])
        from_currency = parts[1].upper()
        to_currency = parts[2].upper()
        
        result = await Frankfurter.get_currency_rate(amount, from_currency, to_currency)
        
        await message.answer(f"💵 {amount} {from_currency} = {result:.2f} {to_currency}")

        await state.clear()
        
    except ValueError:
        await message.answer(f"❌ Ошибка: {result}\n\nПример правильного формата:\n100 USD EUR")
    
    except Exception:
        await message.answer("❌ Ошибка: Неизвестная.")