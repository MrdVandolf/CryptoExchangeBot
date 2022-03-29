from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import db
from handlers.users import direct_to_manager
from keyboards.inline.start_keyboard import start_choice, start_choice_manager


async def handle_transaction(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    crypto_amount = int(message.text)
    tid = message.from_user.id
    full_name = message.from_user.full_name
    user_name = message.from_user.username

    transaction_id = await db.add_transaction(tid, full_name, user_name, current_state, crypto_amount)
    await direct_to_manager.redirect(message, state, trid=transaction_id)
    await user_after_redirect(message, state, transaction_id)


async def user_after_redirect(message: types.Message, state: FSMContext, trid: int):
    await state.finish()
    markup = start_choice_manager if db.has_manager(message.from_user.id) else start_choice
    await message.answer("Ваш запрос успешно отправлен нашим менеджерам! Вскоре они свяжутся"
                         " с вами и помогут совершить сделку.\n"
                         f"Ваш запрос на сделку - {trid}\n"
                         "Обязательно спросите у менеджера номер заявки (сделки), которую"
                         "он обрабатывает, чтобы избежать мошенников!", reply_markup=markup)
