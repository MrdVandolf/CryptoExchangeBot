from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_data import set_crypto_amount


crypto_amount_board = ReplyKeyboardMarkup(row_width=3,
                                           keyboard=[[
                                              KeyboardButton(text="1"),
                                              KeyboardButton(text="10"),
                                              KeyboardButton(text="100"),
                                           ]])
