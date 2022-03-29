from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from keyboards.inline.callback_data import buy_crypto, sell_crypto, get_course


start_choice = ReplyKeyboardMarkup(row_width=2,
                                    keyboard=[
                                        [
                                            KeyboardButton(
                                                text="Купить криптовалюту"
                                            ),
                                            KeyboardButton(
                                                text="Продать криптовалюту"
                                            )
                                        ],
                                        [
                                            KeyboardButton(
                                                text="Курс криптовалюты"
                                            )
                                        ]
                                    ])


start_choice_manager = ReplyKeyboardMarkup(row_width=2,
                                    keyboard=[
                                        [
                                            KeyboardButton(
                                                text="Купить криптовалюту"
                                            ),
                                            KeyboardButton(
                                                text="Продать криптовалюту"
                                            )
                                        ],
                                        [
                                            KeyboardButton(
                                                text="Курс криптовалюты"
                                            ),
                                            KeyboardButton(
                                                text="Обработать запрос на сделку"
                                            )
                                        ]
                                    ])

removal = ReplyKeyboardRemove()