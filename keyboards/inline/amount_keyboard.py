from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_data import set_crypto_amount

crypto_amount_board_give = ReplyKeyboardMarkup(row_width=3,
                                               keyboard=[[
                                                   KeyboardButton(text="5-19"),
                                                   KeyboardButton(text="20-49"),
                                                   KeyboardButton(text="50+"),
                                               ]])

crypto_amount_board_get = ReplyKeyboardMarkup(row_width=2,
                                              keyboard=[[
                                                  KeyboardButton(text="5-19"),
                                                  KeyboardButton(text="20-49"),
                                                  KeyboardButton(text="50-99"),
                                                  KeyboardButton(text="100+"),
                                              ]])
