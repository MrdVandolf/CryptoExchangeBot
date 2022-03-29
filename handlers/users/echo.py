from aiogram import types
from aiogram.dispatcher import FSMContext
import logging

from loader import dp, db
from utils.misc.functions import is_number, is_valid_manager_password
from handlers.users import give_get, course, direct_to_manager, manager, transaction_handler, course_handler
from keyboards.inline.start_keyboard import start_choice, start_choice_manager
from data.global_messages import *


@dp.message_handler(state="*")
async def general(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == "Processing":
        if message.text == request_cancelled:
            logging.info("Cancel request")
            await direct_to_manager.cancel_request(message, state)
        elif message.text == request_completed:
            logging.info("Complete request")
            await direct_to_manager.complete_request(message, state)
        elif message.text == request_in_process:
            logging.info("Request left in process for now")
            await direct_to_manager.leave_in_process(message, state)

    elif current_state in ["Cancelling", "Completing"]:
        logging.info("Choosing request to complete/cancel")
        await direct_to_manager.try_to_finish(message, state)

    elif current_state == "AddingCourse":
        logging.info("Try to add course")
        await process_new_course(message, state)

    elif current_state == "RemovingCourse":
        logging.info("Try to remove course")
        await process_removing_course(message, state)

    elif message.text == manager_process_request and await db.has_manager(message.from_user.id):
        logging.info("Getting open request from user")
        await direct_to_manager.get_open_transaction(message, state)

    elif message.text == manager_complete:
        logging.info("Trying to complete in-process task")
        await direct_to_manager.get_processing_requests(message, state, "COMPLETED")

    elif message.text == manager_cancel:
        logging.info("Trying to cancel in-process task")
        await direct_to_manager.get_processing_requests(message, state, "CANCELLED")

    elif message.text == global_buy_crypto:
        logging.info("Trying to buy crypto")
        await give_get.buy_crypto(message, state)

    elif message.text == global_sell_crypto:
        logging.info("Trying to sell crypto")
        await give_get.sell_crypto(message, state)

    elif message.text == global_get_today_course:
        logging.info("Getting todays course")
        await course.get_course(message, state)

    elif message.text == user_contact_manager:
        logging.info("Left a message to manager")
        await process_manager_contact(message, state)

    elif state is None:
        pass

    else:

        if current_state == "Buy":
            logging.info(f"Buying {message.text}")
            if await is_number(message.text):
                logging.info("Buy Ok")
                await transaction_handler.handle_transaction(message, state)
               #await direct_to_manager.redirect(message, state)
            else:
                logging.info("Buy not ok")
                await give_get.incorrect_sell_buy(message, state)

        elif current_state == "Sell":
            logging.info(f"Selling {message.text}")
            if await is_number(message.text):
                logging.info("Sell Ok")
                await transaction_handler.handle_transaction(message, state)
                #await direct_to_manager.redirect(message, state)
            else:
                logging.info("Sell not ok")
                await give_get.incorrect_sell_buy(message, state)

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


async def process_new_course(message: types.Message, state: FSMContext):
    await db.add_course(message.text)
    await message.answer("Курс успешно добавлен!", reply_markup=start_choice_manager)
    await state.finish()


async def process_removing_course(message: types.Message, state: FSMContext):
    has_this_id = await db.has_course(int(message.text))
    if has_this_id:
        await db.remove_course(int(message.text))
        await state.finish()
        await message.answer("Курс успешно удален!", reply_markup=start_choice_manager)
    else:
        await message.answer("Нет курса с таким id.")
        await course_handler.remove_course(message, state)


async def process_manager_contact(message: types.Message, state: FSMContext):
    manager_username = await db.get_any_manager_contact()
    await message.answer(f"Опишите вашу ситуацию нашему менеджеру - @{manager_username} - в личном сообщении."
                         f" Менеджер ответи в ближайшее время!")