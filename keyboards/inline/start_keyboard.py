from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from keyboards.inline.callback_data import buy_crypto, sell_crypto, get_course


start_choice = ReplyKeyboardMarkup(row_width=2,
                                    keyboard=[
                                        [
                                            KeyboardButton(
                                                text="Получить крипту"
                                            ),
                                            KeyboardButton(
                                                text="Отдать крипту"
                                            )
                                        ],
                                        [
                                            KeyboardButton(
                                                text="Курс крипты"
                                            )
                                        ]
                                    ])

"""
start_choice = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Получить крипту",
                                                callback_data=buy_crypto.new("buy")
                                            ),
                                            InlineKeyboardButton(
                                                text="Отдать крипту",
                                                callback_data=sell_crypto.new("sell")
                                            )
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Курс крипты",
                                                callback_data=get_course.new("course")
                                            )
                                        ]
                                    ]

)
"""
