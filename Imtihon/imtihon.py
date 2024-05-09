from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
import asyncio
import logging
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F
from db import create_user, get_data

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7156760678:AAE4uYHSJMsDIjmXFg-ztm7bs7LHOUfGkqE')
admin_chat_id = 2129817198

from_router = Router()

dp = Dispatcher()

def inline_button():
    buttons = InlineKeyboardBuilder()
    ha = InlineKeyboardButton(text="ha", callback_data="ha")
    yoq = InlineKeyboardButton(text="yoq", callback_data="yoq")
    buttons.add(ha, yoq)
    return buttons.as_markup()
class Kurs(StatesGroup):
    nomi = State()
    narxi = State()
    full_data = State()
    teacher = State()
    

def reply_buttons():
    buttons = [
        [KeyboardButton(text="O'quv kurslar"),KeyboardButton(text="Bizning afzaliklarimiz"), KeyboardButton(text='Kurs qoshish')],
        
    ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)

def inline_data():
     
#  for user in users:
     buttons = InlineKeyboardBuilder()                               
     a = InlineKeyboardButton(text="Fronted", callback_data="fronted")
     b = InlineKeyboardButton(text="Backend", callback_data="backend")
    # c = InlineKeyboardButton(text=f"{user[0]}", callback_data="backend")
     users = get_data()  # Bu funksiya sizning bazangizdan kurs ma'lumotlarini olishni taxmin qiladi
    
     for user in users:
         c = InlineKeyboardButton(text=f"{user[0]}", callback_data=f"course_{user[0]}")
         buttons.add(c)   
     buttons.add(a)
     buttons.add(b)
    # buttons.add(c)
     return buttons.as_markup()

@from_router.message(Command('start'))
async def start(message: types.Message):
   print(message.chat.id)
   await message.answer(f'Assalomu alaykum Hurmatli {message.from_user.first_name}!', reply_markup=reply_buttons())

@from_router.message(lambda message: message.text =="Bizning afzaliklarimiz")
async def get_info(message: types.Message):
    await message.answer("Bizning afzaliklarimiz quydagilar..........")

@from_router.message(lambda message: message.text =="O'quv kurslar")
async def get_info(message: types.Message):
    await message.answer(f"O'quv kurslari", reply_markup=inline_data())
    

@from_router.message(F.text == 'Kurs qoshish')
async def get_nomi(message: types.Message, state: FSMContext):
    if message.chat.id != admin_chat_id:
        return await message.answer("Bu paneldan faqat admin foydalana oladi!!!")
    text = """Kurs nomini kiriting:
    """
    await message.answer(text=text)
    await state.set_state(Kurs.nomi)
        
    
@from_router.message(Kurs.nomi)
async def set_user_name(message: types.Message, state: FSMContext):
    await state.update_data(nomi=message.text)  
    text = """Kurs narxini kiriting:
    """  
    await message.answer(text)
    await state.set_state(Kurs.narxi)




@from_router.message(Kurs.narxi)
async def set_price(message: types.Message, state: FSMContext):
    
    await state.update_data(narxi=message.text)
    text = """Kurs haqida ma'lumot kiriting:
    """
    await message.answer(text=text)
    await state.set_state(Kurs.full_data)



@from_router.message(Kurs.full_data)
async def set_full_data(message: types.Message, state: FSMContext):
    await state.update_data(full_data=message.text)
    text = """Oqituvchi haqida ma'lumot kiriting:
    """
    await message.answer(text=text)
    await state.set_state(Kurs.teacher)


@from_router.message(Kurs.teacher, F.text == "Ha" or "Yo'q")
async def send_application(message: types.Message, state: FSMContext):
    if message.text == "Yo'q":
        return await message.answer(f"Ma'lumotlar yuborilmadi !!!")

    data = await state.get_data()
    text = f"""
    Kurs nomi: {data['nomi']}
    Kurs narxi: {data['narxi']}
    Kurs haqida: {data['full_data']} 
    Oqituvchi haqida: {data['teacher']} 
    """
    create_user(data["nomi"], data["narxi"], data["full_data"], data["teacher"])
    await state.clear()
    await bot.send_message(chat_id=2129817198, text=text)
    await message.answer(f"Ma'lumotlar bazaga joylandi",reply_markup=reply_buttons())




@from_router.message(Kurs.teacher)
async def set_tacher(message: types.Message, state: FSMContext):

    reply_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ha"), KeyboardButton(text='Yo\'q')],
        ],resize_keyboard=True
    )


    await state.update_data(teacher=message.text)
    data = await state.get_data()
    print(data)
    text =text = f"""
    Kurs nomi: {data['nomi']}
    Kurs narxi: {data['narxi']}
    Kurs haqida: {data['full_data']} 
    Oqituvchi haqida: {data['teacher']} 
    """
    await message.answer(text=text, reply_markup=reply_buttons)

async def main():
    dp.include_router(from_router)
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())