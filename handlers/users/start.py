from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import start_choice


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=start_choice)
