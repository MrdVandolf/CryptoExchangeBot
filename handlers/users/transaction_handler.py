from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import db
from handlers.users import direct_to_manager


async def handle_transaction(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    crypto_amount = int(message.text)
    tid = message.from_user.id
    full_name = message.from_user.full_name
    user_name = message.from_user.username

    transaction_id = await db.add_transaction(tid, full_name, user_name, current_state, crypto_amount)
    await direct_to_manager.redirect(message, state)
