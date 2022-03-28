from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("manager"))
async def bot_manage(message: types.Message):
    text = ("Вы - менеджер")

    await message.answer(text)
