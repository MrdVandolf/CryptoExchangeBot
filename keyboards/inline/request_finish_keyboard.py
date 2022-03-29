from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

manager_request_completion = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Завершена"), KeyboardButton(text="Отменена")]]
)