from aiogram import types
from aiogram.dispatcher import FSMContext
import logging

from loader import bot, db
from keyboards.inline import start_choice


async def redirect(message: types.Message, state: FSMContext):
    logging.info("Redirect")
    current_state = await state.get_state()

    request_type = "купить" if current_state == "Buy" else "продать"
    user_nick = f"@{message.from_user.username}"
    user_name = message.from_user.full_name

    managers = await db.get_managers_ids()
    logging.info(f"Менеджеры: {managers}")
    #logging.info(f"Managers: {managers}")

    for i in managers:
        await bot.send_message(chat_id=i, text=f"[МЕНЕДЖЕРУ] {user_name} ({user_nick}) хочет "
                                               f"{request_type} {message.text} криптовалюты")
    await user_after_redirect(message, state)


async def user_after_redirect(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ваш запрос успешно отправлен нашим менеджерам! Вскоре они свяжутся"
                         " с вами и помогут совершить сделку", reply_markup=start_choice)
