from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import buy_crypto, sell_crypto, crypto_amount_board


@dp.callback_query_handler(sell_crypto.filter(callback_info="sell"), state="*")
async def call_give_crypto(call: types.CallbackQuery, state: FSMContext):
    await give_crypto(call.message, state)


@dp.callback_query_handler(buy_crypto.filter(callback_info="buy"), state="*")
async def call_get_crypto(call: types.CallbackQuery, state: FSMContext):
    await get_crypto(call.message, state)


async def incorrect_give_get(message: types.Message, state: FSMContext):
    await message.answer("Некорректный ввод. Пожалуйста, введите только число")
    current_state = await state.get_state()
    if current_state == "Buy":
        await get_crypto(message, state)
    elif current_state == "Sell":
        await give_crypto(message, state)


@dp.message_handler(Command("give"), state="*")
async def give_crypto(message: types.Message, state: FSMContext):
    text = 'Вы хотите отдать крипту. Выберите количество'
    markup = crypto_amount_board
    await state.set_state("Sell")
    await message.answer(text, reply_markup=markup)


@dp.message_handler(Command("get"), state="*")
async def get_crypto(message: types.Message, state: FSMContext):
    text = 'Вы хотите получить крипту. Выберите количество'
    markup = crypto_amount_board
    await state.set_state("Buy")
    await message.answer(text, reply_markup=markup)