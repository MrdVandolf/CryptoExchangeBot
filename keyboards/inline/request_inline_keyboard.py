from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

request_callback = CallbackData("request_process", "request_id")


def generate_markup(rid):
    mp = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[[InlineKeyboardButton("Провести сделку",
                                                                     callback_data=request_callback.new(str(rid)))]])
    return mp