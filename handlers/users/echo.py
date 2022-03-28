from aiogram import types
from aiogram.dispatcher import FSMContext
import logging

from loader import dp
from utils.misc.functions import is_number, is_valid_manager_password
from handlers.users import give_get, course, direct_to_manager, manager


@dp.message_handler(state="*")
async def go_buy(message: types.Message, state: FSMContext):

    if message.text == "Купить криптовалюту":
        await give_get.get_crypto(message, state)

    elif message.text == "Продать криптовалюту":
        await give_get.give_crypto(message, state)

    elif message.text == "Курс криптовалюты":
        await course.get_course(message, state)

    elif state is None:
        pass

    else:
        current_state = await state.get_state()

        if current_state == "Buy":
            logging.info(f"Buying {message.text}")
            if await is_number(message.text):
                logging.info("Buy Ok")
                await direct_to_manager.redirect(message, state)
            else:
                await give_get.incorrect_give_get(message, state)

        elif current_state == "Sell":
            logging.info(f"Selling {message.text}")
            if await is_number(message.text):
                logging.info("Sell Ok")
                await direct_to_manager.redirect(message, state)
            else:
                await give_get.incorrect_give_get(message, state)

        elif current_state == "VerifyManager":
            logging.info(f"Verifying manager")
            password = message.text
            if await is_valid_manager_password(password):
                await manager.verify(message, state)
            else:
                await manager.not_verified(message, state)

        else:
            pass


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
