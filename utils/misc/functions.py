from data import config


async def is_number(val: str):
    diapazon = val in ['5-19', '20-49', '50+', '50-99', '100+']
    isdig = val.isdigit()
    return diapazon or isdig


async def is_valid_manager_password(val: str):
    return val == config.MANAGER_PASS


async def form_the_request_message(info):
    type = "продажу" if info["type"] == "Sell" else "покупку"
    res = f"Вы обрабатываете сделку №{info['id']}\n" \
          f"Вторая сторона: {info['full_name']} (@{info['user_name']})\n" \
          f"Запрос на {type} {info['amount']} токенов криптовалюты.\n" \
          f"Если пользователь отменил сделку, введите 'Отменена'\n" \
          f"Если сделка проведена успешно, введите 'Завершена'\n"

    return res


async def get_request_info(info):
    type = "продажу" if info["type"] == "Sell" else "покупку"
    res = f"Сделка №{info['id']}\n" \
          f"Вторая сторона: {info['full_name']} (@{info['user_name']})\n" \
          f"Запрос на {type} {info['amount']} токенов криптовалюты.\n"
    return res
