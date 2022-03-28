from data import config


async def is_number(val: str):
    return val.isdigit()


async def is_valid_manager_password(val: str):
    return val == config.MANAGER_PASS