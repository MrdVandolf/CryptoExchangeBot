from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            #types.BotCommand("help", "Вывести справку"),
            types.BotCommand("manager", "Зайти как менеджер"),
           # types.BotCommand("give", "Запрос на продажу криптовалюты"),
            #types.BotCommand("get", "Запрос на получение криптовалюты"),
           # types.BotCommand("course", "Получить курс криптовалюты"),
           # types.BotCommand("finish_state", "Закончить состояние"),
            types.BotCommand("add_course", "Добавить новый курс валют"),
            #types.BotCommand("edit_course", "Изменить существующий курс валют"),
            types.BotCommand("remove_course", "Удалить существующий курс валют")
        ]
    )
