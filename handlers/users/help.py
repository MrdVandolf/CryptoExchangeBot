from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    if await db.has_manager(message.from_user.id):
        await message.answer("/add_course - добавить новый курс. После ввода команды нужно будет ввести текст нового"
                             " курса.\n/remove_course - удалить существующий курс. После ввода команды нужно будет"
                             " ввести id (ТОЛЬКО ЧИСЛО) удаляемого курса.")
    
    else:
        await message.answer("Это - бот-криптообменник.\nС его помощью вы можете получить или отдать"
                             " токены MOST. Вам надо нажать на кнопку Получить/Отдать Most Token, выбрать"
                             " количество токенов и ваш запрос на сделку будет передан нашим квалифицированным"
                             " менеджерам, которые с вами свяжутся!\n"
                             "/start - начать общение с ботом\n"
                             "/help - справка о боте\n"
                             "/manager - зайти как менеджер (понадобится ввод пароля)")
