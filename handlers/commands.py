# Aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext

# Keyboard
from keyboards.general import Menu_Keyboard

# Local
from basic import log


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    log(message.from_user.username, "--start--")

    await message.answer(
        text="Choose one option",
        reply_markup=Menu_Keyboard
    )
    await state.set_state('menu')
