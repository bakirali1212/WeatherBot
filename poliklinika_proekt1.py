from aiogram import types, Bot, Dispatcher, Router
import asyncio
from aiogram.filters import Command
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



logging.basicConfig(level=logging.INFO)
bot = Bot(token="7064526501:AAF6lSQkU5otJVlEDL9V_7T4jbyH5Jk-zQA")

from_router = Router()
dp = Dispatcher()

@dp.message(Command('start'))
async def get_started(message: types.Message):
    full_name = message.from_user.full_name
    button = types.KeyboardButton(text= "Poliklinikalar") 
    button1 = types.KeyboardButton(text= "/start")
    buttons = types.ReplyKeyboardMarkup(
            keyboard=[[button1,button]],
            resize_keyboard=True)
    await message.answer(f"Assalomu alaykum, {full_name}", reply_markup=buttons)

async def main():
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())