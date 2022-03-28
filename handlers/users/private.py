from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(Command("finish_state"), state="*")
async def finish_state(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Состояние завершено")
