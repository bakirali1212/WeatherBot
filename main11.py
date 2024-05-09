
from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import F
from random import randint
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

bot = Bot(token="6823964127:AAH9LPbbtWbaResMwanHkCe3rWbdtTIefk0")

dp = Dispatcher()

def reply_buttons():
    buttons = [
        [KeyboardButton(text="/url", url="..."),KeyboardButton(text="Telefon raqam",request_contact=True)],
        [KeyboardButton(text="Mening malumotlarim"),KeyboardButton(text="random son")]
        [KeyboardButton(text="Support"),KeyboardButton(text="Locotion", request_location=True)]
    ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)

def inline_data():
     buttons = InlineKeyboardBuilder()                               #https://www.instagram.com/bakirali_12_11/#
     a = InlineKeyboardButton(text="Mening instagram sahifam",url="https://www.instagram.com/bakirali_12_11/#", callback_data="instagram")
     b = InlineKeyboardButton(text="Mening telegram profilm",url="https://t.me/bakirali_zokirov", callback_data="telegram")

     buttons.add(a)
     buttons.add(b)
     return buttons.as_markup()

    
def inline_buttons():
    buttons = InlineKeyboardBuilder()
    a = InlineKeyboardButton(text="random son", callback_data="random_son")
    b = InlineKeyboardButton(text="random rasm", callback_data="random_rasm")

    buttons.add(a)
    buttons.add(b)
    #buttons.add(InlineKeyboardButton(text="random rasm", callback_data="random_rasm"))
    return buttons.as_markup()

@dp.message(Command("start"))
async def start_bot(message: Message):
    # print(message.chat.id)
    # print(message.from_user.first_name)
    await message.answer(f"Assalom Aleykum, xush kelbsiz {message.from_user.first_name}!",reply_markup = reply_buttons())

@dp.message(F.text == "Mening malumotlarim")
async def generate_random(message: Message):                           
    await message.answer(text=f"Mening ismim {message.from_user.first_name},\n yoshim 19,\n tug'ilgan sanam 2004.11.12", reply_markup=inline_data())

@dp.message(F.text == "random son")
async def generate_random(message: Message):                           #random son uchun yozilgan funksiya
    await message.answer(text=f"random son: {randint(1,10)}", reply_markup=inline_buttons())

@dp.callback_query()
async def callback_answer(callback: types.CallbackQuery):
    print(callback.data)
    if callback.data == "telegram":
        await callback.answer(text=f"telegram")

@dp.callback_query()
async def callback_answer(callback: types.CallbackQuery):
    print(callback.data)
    if callback.data == "instagram":
        await callback.answer(text=f"instagram")


async def main():
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())