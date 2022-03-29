from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from loader import dp, db
from keyboards.inline.start_keyboard import removal


@dp.message_handler(Command("add_course"), state="*")
async def add_course(message: types.Message, state: FSMContext):
    if await db.has_manager(message.from_user.id):
        await state.set_state("AddingCourse")
        await message.answer("Введите курс валюты\n Например: 1 USDT = 0.9 GMT", reply_markup=removal)
    else:
        await message.answer("Недостаточно прав для этого действия")


@dp.message_handler(Command("edit_course"), state="*")
async def edit_course(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(Command("remove_course"), state="*")
async def remove_course(message: types.Message, state: FSMContext):
    if await db.has_manager(message.from_user.id):
        info = await db.get_courses()
        if len(info) > 0:
            await state.set_state("RemovingCourse")
            text = "Впишите id курса, который вы хотите удалить:\n"
            for i in range(len(info)):
                text += f"{info[i]['course']} (id={info[i]['id']})\n"
            await message.answer(text, reply_markup=removal, parse_mode=ParseMode.MARKDOWN)