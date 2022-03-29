from aiogram import types
from aiogram.dispatcher import FSMContext
import logging

from loader import bot, db, dp
from utils.misc.functions import form_the_request_message
from keyboards.inline.request_inline_keyboard import generate_markup, request_callback
from keyboards.inline.request_finish_keyboard import manager_request_completion
from keyboards.inline.start_keyboard import start_choice_manager


async def redirect(message: types.Message, state: FSMContext, trid: int = 0):
    logging.info("Redirect")
    current_state = await state.get_state()

    request_type = "покупку" if current_state == "Buy" else "продажу"
    #user_nick = f"@{message.from_user.username}"
    #user_name = message.from_user.full_name

    managers = await db.get_managers_ids()
    logging.info(f"Менеджеры: {managers}")
    #logging.info(f"Managers: {managers}")

    markup = generate_markup(trid)
    for i in managers:
        await bot.send_message(chat_id=i, text=f"[МЕНЕДЖЕРУ] запрос на "
                                               f"{request_type} {message.text} криптовалюты",
                               reply_markup=markup)


async def get_open_transaction(message: types.Message, state: FSMContext):
    tid = await db.get_open_transaction_id()
    if tid is None:
        await message.answer("Нет открытых запросов на сделку")
    else:
        await process_transaction(message, state, tid)


@dp.callback_query_handler(request_callback.filter())
async def process_callback_transaction(call: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()

    if current_state != "Processing":
        trans_id = int(call.data.split(':')[1])
        await process_transaction(call.message, state, trans_id)


async def process_transaction(message: types.Message, state: FSMContext, trans_id: int):
    trans_status = await db.get_transaction_status(trans_id)

    if trans_status == "OPEN":
        await state.set_state("Processing")
        await state.update_data(transaction_id=trans_id)
        manager_id = str(message.chat.id)
        await db.change_transaction_status(trans_id, "PROCESSING", manager_id)
        info = await db.get_transaction(trans_id)
        text = await form_the_request_message(info)
        await message.answer(text, reply_markup=manager_request_completion)

    elif trans_status == "PROCESSING":
        await message.edit_text(text="Сделка уже обрабатывается", reply_markup=None)

    elif trans_status == "CANCELLED":
        await message.edit_text(text="Сделка отменена", reply_markup=None)

    elif trans_status == "COMPLETED":
        await message.edit_text(text="Сделка завершена", reply_markup=None)


async def cancel_request(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Сделка №{data['transaction_id']} была отменена.", reply_markup=start_choice_manager)
    await db.change_transaction_status(data['transaction_id'], "CANCELLED")
    await state.finish()


async def complete_request(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Сделка №{data['transaction_id']} была завершена.", reply_markup=start_choice_manager)
    await db.change_transaction_status(data['transaction_id'], "COMPLETED")
    await state.finish()