import random
import csv
import sqlite3
from db import BotDB
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

###############################################################################################
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="5104763927:AAEc4bkq7nWqVKzeXOu-YF_Z5SjotTZn_7w")

# Диспетчер для бота

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

str1 = []

with open("tpbook3.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter=";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            pass
            # print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            # print(f'    {row[0]} - {row[1]} - {row[2]} -.')
            str1.append(row[0] + " " + row[1] + " " + row[2] + "\n")
        count += 1

# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()


def nt(str1):
    answer = random.choice(str1)
    return answer

import aiogram.utils.markdown as fmt

# Загружаем список поговорок
f = open('data/telefon.txt', 'r', encoding='UTF-8')
telf = f.read().split('\n')
f.close()

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

BotDB = BotDB('accountant.db')

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Информация об УПЦ 👋')
button_tf = KeyboardButton('Телефонная книга УПЦ')
button_an = KeyboardButton('Анекдот')

greet_kb = ReplyKeyboardMarkup()

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi).add(button_tf).add(button_an)

def keyboard(kb_config):
    _keyboard = types.InlineKeyboardMarkup()

    for rows in kb_config:
        btn = types.InlineKeyboardButton(
            callback_data=rows[0],
            text=rows[1]
        )
        _keyboard.insert(btn)

    return _keyboard


@dp.callback_query_handler()
async def callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text=callback_query.data)
    await bot.send_message(callback_query.from_user.id, text=callback_query.data)


def anekd():
    connection = sqlite3.connect('anekdot.db')
    cursor = connection.cursor()
    z = random.randrange(1, 9000, 1)
    cursor.execute('SELECT * FROM anekdot WHERE rowid=' + str(z))
    row = cursor.fetchone()
    connection.close()
    return row[1]


strupc = "Учебно-производственный центр — один из лидеров образовательных подразделений ПАО «Газпром» в реализации " \
         "системы фирменного профессионального образования персонала, является школой инженерной культуры. В " \
         "структуре ООО «Газпром трансгаз Югорск» Учебно-производственный центр функционирует с 1979 года. \nВ центре " \
         "проводится обучение и развитие руководителей и специалистов компании, повышение квалификации, " \
         "профессиональная переподготовка, предаттестационная подготовка и аттестация, оценочные и развивающие " \
         "мероприятия, тематические и консультационные семинары, дистанционное обучение. "


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Этот информационный бот УПЦ.\n Это справочник телефонных номеров УПЦ.",
                        reply_markup=greet_kb)
    await message.reply(anekd(), reply_markup=greet_kb)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://lolkot.ru/lolmixer/gallery/images/90d57bdba0f87df670914f90a858b76a1374987601.jpg",
        # reply_markup=keyboard([
        #     [message.from_user.id, "кнопка1", "/f" + "ПЕР", None],
        #     ["22", "кнопка2", "текст сообщения", None],
        #     ["32", "кнопка3", "текст сообщения", None]
        # ]),
        caption="Телефонная книга УПЦ. Для поиска телефона нажмите кнопку меню, нажмите Найти и подержите две секунды."
    )
@dp.message_handler(commands=['f'])
async def process_start_command(message: types.Message):
    fn = message.text
    if (message.text != ""):
        s = message.text.split()
        if (len(s) > 1):
            fn = s[1]
    await message.answer(
        fmt.text(
            fmt.text(process.extractOne(fn, str1)[0]),
            fmt.text(process.extract(fn, str1)),
            # fmt.text(process.extractOne(fn, str1[2])),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(content_types=['text'])
async def ande1(message: types.Message):
    if (message.text == "Информация об УПЦ 👋"):
        await message.reply(strupc, reply_markup=greet_kb)
    if (message.text == "Анекдот"):
        await message.reply(anekd(), reply_markup=greet_kb)
    if (message.text == "Телефонная книга УПЦ"):
        for i in str1:
            await message.reply(i, reply_markup=greet_kb)

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb)

# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
