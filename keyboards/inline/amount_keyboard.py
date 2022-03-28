from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_data import set_crypto_amount


crypto_amount_board = ReplyKeyboardMarkup(row_width=3,
                                           keyboard=[[
                                              KeyboardButton(text="1"),
                                              KeyboardButton(text="10"),
                                              KeyboardButton(text="100"),
                                           ]])

'''
crypto_amount_board = InlineKeyboardMarkup(row_width=3,
                                           inline_keyboard=[[
                                              InlineKeyboardButton(text="1",
                                                                   callback_data=set_crypto_amount.new("1")),
                                              InlineKeyboardButton(text="10",
                                                                   callback_data=set_crypto_amount.new("10")),
                                              InlineKeyboardButton(text="100",
                                                                   callback_data=set_crypto_amount.new("100")),
                                           ]])
'''