from aiogram import types
from main_help import bot
from main_help import dp

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)