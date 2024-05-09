import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import re
# import sqlite3

# connection = sqlite3.connect('test.db') # muloqot o'rnatish

# cursor = connection.cursor()



PHONE_PATTERN = r"\+998[0-9]{9}"

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7064526501:AAG6ty1QS1WsVswjJYPmhgrEcrh7_iveTvM')

from_router = Router()

dp = Dispatcher()

class Registration(StatesGroup):
    full_name = State()
    age = State()
    gender = State()
    telefon_raqam = State()
    maqsad = State()
class Registration1(StatesGroup):
    full_name = State()
    age = State()
    gender = State()
    telefon_raqam = State()
    maqsad = State()



def reply_buttons():
    buttons = [
        [KeyboardButton(text="Русский язык"),KeyboardButton(text="Uzbek tili")],
        
    ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def registration_buttons():
    buttons = [
        [KeyboardButton(text="Зарегистрироваться")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def registration1_buttons():
    buttons = [
        [KeyboardButton(text="Royxatga olish")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def next_buttons():
    buttons = [
        [KeyboardButton(text="следуш")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def next1_buttons():
    buttons = [
        [KeyboardButton(text="next")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def boshqa_buttons():
    buttons = [
        [KeyboardButton(text="другой")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)
def boshqa1_buttons():
    buttons = [
        [KeyboardButton(text="boshqa")],
        ]
    return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard=True)

@from_router.message(Command('start'))
async def start(message: types.Message):
   await message.answer(f'Tilni tanlang:\nВыберите язык:', reply_markup=reply_buttons())

@from_router.message(F.text == 'Русский язык')
async def select_language(message: types.Message):
    await message.answer(f"Нажмите кнопку «Зарегистрироваться» и зарегистрируйтесь", reply_markup=registration_buttons())



@from_router.message(F.text == 'Зарегистрироваться')
async def set_full_name(message: types.Message, state: FSMContext):
    text = """Введите свою полную фамилию, 
     например: Закиорв Бакирали Абдужалил оглу.

    """
    await message.answer(text=text)
    await state.set_state(Registration.full_name)

@from_router.message(Registration.full_name)
async def set_user_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = """Введите свой возраст. 
    например 20
    
    """
    await message.answer(text)
    await state.set_state(Registration.age)

@from_router.message(Registration.age)
async def set_user_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("возраст должен быть только цифрами")
    await state.update_data(age=message.text)
    text = """ваш пол:

    """
    await message.answer(text)
    await state.set_state(Registration.gender)

@from_router.message(Registration.gender)
async def set_user_texnogy(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    text = """Контакт:

     Введите свой контактный номер?
     Например +998901234567
    """
    await message.answer(text)
    await state.set_state(Registration.telefon_raqam)

@from_router.message(Registration.telefon_raqam)
async def set_user_number(message: types.Message, state: FSMContext):
    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer("Убедитесь, что это номер Узбекистана!!!")
    await state.update_data(telefon_raqam=message.text)
    text = """Какова цель вашего визита?
    """
    await message.answer(text)
    await state.set_state(Registration.maqsad)


    
@from_router.message(Registration.maqsad)
async def set_user_number(message: types.Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    print(data)
    text = f"""Foydalanuvchi: {data['full_name']}
     Yosh: {data['age']}
     Jinsi: {data['gender']} 
    🇺🇿 Telegram: @{message.from_user.username}
    📞 Aloqa: {data['telefon_raqam']}
    🔎 Maqsad: {data['maqsad']}
    """
    await message.answer(text=text)
    await state.clear()
    return await message.answer(f"Вы успешно завершили регистрацию!!! ",reply_markup=next_buttons())
    

@from_router.message(F.text == 'следуш')
async def select_language(message: types.Message):
    await message.answer(f"""Что может сделать для вас бот Telegram?
1) В списке какой семейной поликлиники вы находитесь ?
2) вы владеете информацией о видах услуг, оказываемых врачами.
3) Вы можете узнать рабочие дни, режим работы и фамилии всех врачей.
4) Вы можете записаться на прием к врачам онлайн.""", reply_markup=boshqa_buttons())
    
@from_router.message(F.text == 'Uzbek tili')
async def select_language(message: types.Message):
    await message.answer(f"Ro'yxatdan olish tugmasini bosing va ro'yxatdan o'ting", reply_markup=registration1_buttons())

@from_router.message(F.text == 'Royxatga olish')
async def set_full_name(message: types.Message, state: FSMContext):
    text = """To'liq familiyangizni kiriting,
     masalan: Zakiorv Bakirali Abdujalil o‘g‘li.

    """
    await message.answer(text=text)
    await state.set_state(Registration1.full_name)

@from_router.message(Registration1.full_name)
async def set_user_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = """Yoshingizni kiriting.
     masalan: 20
    
    """
    await message.answer(text)
    await state.set_state(Registration1.age)

@from_router.message(Registration1.age)
async def set_user_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("yoshi faqat raqamlar bo'lishi kerak")
    await state.update_data(age=message.text)
    text = """Sizning jinsingiz:

    """
    await message.answer(text)
    await state.set_state(Registration1.gender)

@from_router.message(Registration1.gender)
async def set_user_texnogy(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    text = """Aloqa:

      Aloqa raqamingizni kiritingmi?
      Masalan, +998901234567
    """
    await message.answer(text)
    await state.set_state(Registration1.telefon_raqam)

@from_router.message(Registration1.telefon_raqam)
async def set_user_number(message: types.Message, state: FSMContext):
    if not re.match(PHONE_PATTERN, message.text):
        return await message.answer("Bu O'zbekiston raqami ekanligiga ishonch hosil qiling!!!")
    await state.update_data(telefon_raqam=message.text)
    text = """maqsadingizni yozib qoldiring.
    """
    await message.answer(text)
    await state.set_state(Registration1.maqsad)


@from_router.message(Registration1.maqsad, F.text == "HA" or "YOQ")
async def send_aplication(message: types.Message, state: FSMContext):
   if message.text == "YOQ":
        return await message.answer(f"")

@from_router.message(Registration1.maqsad)
async def set_user_number(message: types.Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    print(data)
    reply_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="HA"), KeyboardButton(text="YOQ")],
        ],resize_keyboard=True
    )
    text = f"""Foydalanuvchi: {data['full_name']}
     Yosh: {data['age']}
     Jinsi: {data['gender']} 
    🇺🇿 Telegram: @{message.from_user.username}
    📞 Aloqa: {data['telefon_raqam']}
    🔎 Maqsad: {data['maqsad']}
    # """
    await message.answer(text=text, reply_markup=reply_buttons)
    await state.clear()
    return await message.answer(f"Siz roʻyxatdan oʻtishni muvaffaqiyatli yakunladingiz!!!",reply_markup=next1_buttons())

    

@from_router.message(F.text == 'next')
async def select_language(message: types.Message):
    await message.answer(f"""Telegram bot siz uchun nima qilishi mumkin?
1) Siz qaysi oilaviy poliklinika ro'yxatidasiz?
2) shifokorlar tomonidan ko'rsatiladigan xizmatlar turlari haqida ma'lumotga ega bo'lsangiz.
3) Siz barcha shifokorlarning ish kunlari, ish vaqti va ismlarini bilib olishingiz mumkin.
4) Siz onlayn shifokorlar bilan uchrashishingiz mumkin.""", reply_markup=boshqa1_buttons())


async def main():
    dp.include_router(from_router)
    print("Bot sucessfully started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS student (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                full_name VARCHAR(60) NOT NULL,
#                age INTEGER,
#                gender TEXT
#                telefon_raqam TEXT
#                maqsad TEXT

#     )
#     """
# )
# cursor.execute('SELECT * FROM student')
# eski_malumotlar = cursor.fetchall()

    # datas = list(data.values())
    # # datas = message.text.split()
    
    # ful_name = datas[0]
    # age = int(datas[1])
    # gender = datas[2]
    # telefon_raqam = datas[3]
    # maqsad = datas[4]
    # print(datas)
    

    # connection = sqlite3.connect('test.db')
    # cursor = connection.cursor()
    # sql_query = "INSERT INTO student (full_name,age gender, telefon_raqam, maqsad)  VALUES(?, ?, ?, ?, ?, ?)"
    # cursor.execute(sql_query, (ful_name, age, gender, telefon_raqam, maqsad))
    # connection.commit()
    # connection.close()
    # data = message.text.split()
    # ful_name = data['full_name'][:-1]
    # age = int(data['age'])
    # gender = data['gender']
    # Telefon_raqam = data['telefon_raqam']
    # maqsad = data['maqsad']

    # connection = sqlite3.connect('test.db')
    # cursor = connection.cursor()
    # sql_query = "INSERT INTO saqlovchi VALUES(?, ?, ?, ?,?)"
    # values = (ful_name, age, gender, Telefon_raqam, maqsad )
    # cursor.execute(sql_query, values)
    # connection.commit()
    # connection.close()