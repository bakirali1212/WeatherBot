import requests
from pprint import pprint
API_KEY = "268174353272ba89beb58d10ad5d7e0c"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)

    #200 OK, 404 NOT FOUND, 500 API xatolik, 403
    # status_code

    if response.status_code == 200:
        
        data = response.json()
        # pprint(data)
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        namlik = data['main']['humidity']
        tempratura = data['main']['temp']-273
        city_name = data['name']
        country = data['sys']['country']
        weather = data['weather'][0]['main']
        speed = data['wind']['speed']

        text = f"{city_name}({country}) \nTempratura: {tempratura} \nOb-havo holati: {weather} \nNamlik: {namlik} \nTezlik: {speed}"

        return text, latitude, longitude
    

print(get_weather_data('Tashkent'))

from aiogram import types, Bot, Dispatcher, Router
import asyncio
from aiogram.filters import Command
import logging
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


logging.basicConfig(level=logging.INFO)
bot = Bot(token="7156760678:AAE4uYHSJMsDIjmXFg-ztm7bs7LHOUfGkqE")

from_router = Router()
dp = Dispatcher()

@dp.message(Command('start'))
async def get_started(message: types.Message):
    print(message.chat.id)
    if await bot.get_chat_member(chat_id=-1002065430186,user_id=message.from_user.id):


        button = types.KeyboardButton(text= "Ob-havo ma'lumotlari")
        button1 = types.KeyboardButton(text= "/start")
        buttons = types.ReplyKeyboardMarkup(
            keyboard=[[button1],
                    [button]],
                    resize_keyboard=True
        )
    return await message.answer(f"Assalomu alaykum Hurmatli {message.from_user.first_name}", reply_markup=buttons)



@dp.message(lambda message: message.text =="Ob-havo ma'lumotlari")
async def get_weather_info(message: types.Message):
    await message.answer("shahar nomini kiriting")

@dp.message()
async def response_result(message: types.Message):
    city = message.text
    info = get_weather_data(city)
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=info[1],
        longitude=info[2]
    )
    await message.answer(info[0])

async def main():
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())