from aiogram import types
from main_help import dp

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nThis is start")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Hello!\nThis is help")
