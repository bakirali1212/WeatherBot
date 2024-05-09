
from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.filters import Command
import logging
from aiogram import F


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6823964127:AAH9LPbbtWbaResMwanHkCe3rWbdtTIefk0")

form_router =Router()

dp = Dispatcher()


class RegisterForm(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    print(message.chat.id) #2129817198
    await message.answer(text='Assalomu alaykum, Royhatdan otish uchun register deb yozig.')


    # await bot.send_photo(chat_id=message.chat.id, photo="https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    # await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAELdNFl1KXklw47xksFKuxxOJRj6ybrzAAChxUAAj0PUEnem2b91sejvzQE")
    # await bot.send_location(chat_id=message.chat.id, latitude=41.287447591945714, longitude=69.21900048174372)
    # await bot.send_poll(chat_id=message.chat.id,question="vash poll", options=["Erkak",'Ayol'], is_anonymous=False, allows_multiple_answers=True)
    # await bot.send_game()


@dp.message(Command('register'))
async def start_register(message: types.Message, state: FSMContext):
    await message.answer("royxatdatdan otish boshlandi, ismingizni kiriting.")
    await state.set_state(RegisterForm.full_name)

async def main():
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())