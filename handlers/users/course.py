from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards.inline import get_course
from loader import dp


@dp.callback_query_handler(get_course.filter(callback_info="course"), state="*")
async def call_course(call: types.CallbackQuery, state: FSMContext):
    await get_course(call.message, state)


@dp.message_handler(Command("course"), state="*")
async def get_course(message: types.Message, state: FSMContext):
    text = 'Вы хотите узнать курс криптовалют'
    await state.finish()
    await message.answer(text)