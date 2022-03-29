from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from keyboards.inline.callback_data import buy_crypto, sell_crypto, get_course
from data.global_messages import *


start_choice = ReplyKeyboardMarkup(row_width=2,
                                    keyboard=[
                                        [
                                            KeyboardButton(
                                                text=global_buy_crypto
                                            ),
                                            KeyboardButton(
                                                text=global_sell_crypto
                                            )
                                        ],
                                        [
                                            KeyboardButton(
                                                text=global_get_today_course
                                            ),
                                            KeyboardButton(
                                                text=user_contact_manager
                                            )
                                        ]
                                    ])


start_choice_manager = ReplyKeyboardMarkup(row_width=2,
                                    keyboard=[
                                        [
                                            KeyboardButton(
                                                text=global_buy_crypto
                                            ),
                                            KeyboardButton(
                                                text=global_sell_crypto
                                            )
                                        ],
                                        [
                                            KeyboardButton(
                                                text=global_get_today_course
                                            ),
                                            KeyboardButton(
                                                text=manager_process_request
                                            ),
                                            KeyboardButton(
                                                text=manager_process_help
                                            )
                                        ]
                                    ])

removal = ReplyKeyboardRemove()