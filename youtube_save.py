from aiogram import types, Bot, Dispatcher, Router
import asyncio
from aiogram.filters import Command
import logging
from pytube import YouTube
from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup
import requests


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6047875058:AAGCx5J2ky-agcmnhbf3LqNPk0mn-jzlHKM")

from_router = Router()
dp = Dispatcher()

@dp.message(Command('start'))
async def get_started(message: types.Message):
    full_name = message.from_user.full_name
    button = types.KeyboardButton(text= "You tubedan yuklash") 
    button1 = types.KeyboardButton(text= "/start")
    buttons = types.ReplyKeyboardMarkup(
            keyboard=[[button1,button]],
            resize_keyboard=True)
    await message.answer(f"Assalomu alaykum, {full_name}", reply_markup=buttons)

@dp.message(lambda message: message.text =="You tubedan yuklash")
async def get_youtube(message: types.Message):
    await message.answer(f"Video silkasini yuboring. \nHurmatli {message.from_user.full_name}")

@dp.message()
async def  get_video(message: types.Message):
    video_url = message.text
    await message.reply("Videoniz qabul qilindi! Endi uni yuklab olaylik...")
#/get_video_info?video_id={video_url.split('v=')[-1]}
    try:
        r = requests.get(f"https://www.youtube.com/get_video_info?video_id={video_url.split('v=')[-1]}")
        video_info = r.text
        video_url = video_info.split("&url_encoded_fmt_stream_map=url%3D")[1].split("%2Cquality%3D")[0].replace("%3A", ":").replace("%2F", "/").replace("%26", "&")
        await bot.send_video(message.chat.id, video_url)
    except Exception as e:
        logging.error(e)
        await message.reply("Videoni yuklab bo'lmadi. Iltimos, tekshirib qaytadan urinib ko'ring.")


async def main():
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())