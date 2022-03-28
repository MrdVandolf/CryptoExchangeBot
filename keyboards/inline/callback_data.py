from aiogram.utils.callback_data import CallbackData

buy_crypto = CallbackData("buyer", "callback_info")
sell_crypto = CallbackData("seller", "callback_info")
get_course = CallbackData("course", "callback_info")

set_crypto_amount = CallbackData("crypto_amount", "amount")