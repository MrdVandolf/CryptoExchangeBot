from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import start_choice, start_choice_manager


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    markup = start_choice_manager if await db.has_manager(message.from_user.id) else start_choice
    await message.answer(f"Здравствуйте, {message.from_user.full_name}! Я - "
                         f"бот для обмена криптовалюты TKN! Вы можете продать или купить"
                         f" токены с моей помощью! Выберите 'Купить криптовалюту' или 'Продать криптовалюту'"
                         f" и я оставлю ваш запрос на сделку менеджерам, которые с вам свяжутся"
                         f" в скором времени!", reply_markup=markup)
