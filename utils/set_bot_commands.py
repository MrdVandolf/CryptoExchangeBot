from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("manager", "Отметиться как менеджер"),
            types.BotCommand("give", "Запрос на продажу крипты"),
            types.BotCommand("get", "Запрос на получение крипты"),
            types.BotCommand("course", "Получить курс крипты"),
            types.BotCommand("finish_state", "Закончить состояние")
        ]
    )
