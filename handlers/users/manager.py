from aiogram import types
from aiogram.dispatcher.filters import Command

from aiogram.dispatcher import FSMContext

from loader import dp, db
from handlers.users import start


@dp.message_handler(Command("manager"))
async def bot_manage(message: types.Message, state: FSMContext):
    res = await db.has_manager(message.from_user.id)
    if not res:
        await message.answer("Подтвердите, что вы менеджер - введите пароль.")
        await state.set_state("VerifyManager")
    else:
        await message.answer("Вы уже получили статус [МЕНЕДЖЕР]")


async def verify(message: types.Message, state: FSMContext):
    await db.add_manager(message.from_user.id, message.from_user.full_name)
    await message.answer("Вы успешно прошли контроль. Вам присвоен статус [МЕНЕДЖЕР]")
    await start.bot_start(message, state)


async def not_verified(message: types.Message, state: FSMContext):
    await message.answer("Неверный пароль. Попробуйте снова.")