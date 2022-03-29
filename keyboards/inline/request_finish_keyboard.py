from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from data.global_messages import request_completed, request_in_process, request_cancelled

manager_request_completion = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=request_completed),
               KeyboardButton(text=request_in_process),
               KeyboardButton(text=request_cancelled)]]
)