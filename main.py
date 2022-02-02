import random

from aiogram.dispatcher.filters import Command
import csv
from db import BotDB
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
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

#
# # States
# class Form(StatesGroup):
#     name = State()  # Will be represented in storage as 'Form:name'
#     age = State()  # Will be represented in storage as 'Form:age'
#     gender = State()  # Will be represented in storage as 'Form:gender'
#
#
# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message):
#     """
#     Conversation's entry point
#     """
#     # Set state
#     await Form.name.set()
#
#     await message.reply("Hi there! What's your name?")
#
#
# # You can use state '*' if you need to handle all states
# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     logging.info('Cancelling state %r', current_state)
#     # Cancel state and inform user about it
#     await state.finish()
#     # And remove keyboard (just in case)
#     await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())
#
#
# @dp.message_handler(state=Form.name)
# async def process_name(message: types.Message, state: FSMContext):
#     """
#     Process user name
#     """
#     async with state.proxy() as data:
#         data['name'] = message.text
#
#     await Form.next()
#     await message.reply("How old are you?")
#
#
# # Check age. Age gotta be digit
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
# async def process_age_invalid(message: types.Message):
#     """
#     If age is invalid
#     """
#     return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")
#
#
# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     # Update state and data
#     await Form.next()
#     await state.update_data(age=int(message.text))
#
#     # Configure ReplyKeyboardMarkup
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     markup.add("Male", "Female")
#     markup.add("Other")
#
#     await message.reply("What is your gender?", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
# async def process_gender_invalid(message: types.Message):
#     """
#     In this example gender has to be one of: Male, Female, Other.
#     """
#     return await message.reply("Bad gender name. Choose your gender from the keyboard.")
#
#
# @dp.message_handler(state=Form.gender)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gender'] = message.text
#
#         # Remove keyboard
#         markup = types.ReplyKeyboardRemove()
#
#         # And send message
#         await bot.send_message(
#             message.chat.id,
#             md.text(
#                 md.text('Hi! Nice to meet you,', md.bold(data['name'])),
#                 md.text('Age:', md.code(data['age'])),
#                 md.text('Gender:', data['gender']),
#                 sep='\n',
#             ),
#             reply_markup=markup,
#             parse_mode=ParseMode.MARKDOWN,
#         )
#
#     # Finish conversation
#     await state.finish()
#






###########################################################################################

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
button_tf = KeyboardButton('/Телефонная книга УПЦ')

greet_kb = ReplyKeyboardMarkup()

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi).add(button_tf)


# greet_kb= ReplyKeyboardMarkup(resize_keyboard=True).add(button_tf)


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


# @dp.message_handler(commands=['start'])
# async def process_admin_command(message: types.Message):
#     await bot.send_photo(
#        chat_id=message.from_user.id,
#        photo="https://devka.top/uploads/posts/2020-10/1603340966_45-p-mokrie-siski-porno-65.jpg",
#         reply_markup=keyboard([
#             [message.from_user.id, "кнопка1", "/f" + "ПЕР", None],
#             ["22", "кнопка2", "текст сообщения", None],
#             ["32", "кнопка3", "текст сообщения", None]
#         ]),
#         caption="Телефонная книга УПЦ и сиськи"
#     )


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Этот бот создал Юрий Казанцев.\n Это справочник телефонных номеров УПЦ.",
                        reply_markup=greet_kb)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="https://devka.top/uploads/posts/2020-10/1603340966_45-p-mokrie-siski-porno-65.jpg",
        # reply_markup=keyboard([
        #     [message.from_user.id, "кнопка1", "/f" + "ПЕР", None],
        #     ["22", "кнопка2", "текст сообщения", None],
        #     ["32", "кнопка3", "текст сообщения", None]
        # ]),
        caption="Телефонная книга УПЦ и сиськи"
    )


@dp.message_handler(commands=['f'])
async def process_start_command(message: types.Message):
    fn = message.text
    if (message.text != ""):
        s = message.text.split()
        if (len(s) > 1):
            fn = s[1]
    await message.reply(process.extractOne(fn, str1)[0], reply_markup=greet_kb)


@dp.message_handler(commands=['Телефонная книга УПЦ'])
async def process_start_command(message: types.Message):
    fn = "МЕ"
    if (message.text != ""):
        s = message.text.split()
        if (len(s) > 1):
            fn = s[1]
    await message.reply(process.extractOne(fn, str1)[0], reply_markup=greet_kb)





@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb)


@dp.message_handler(commands=['hi2'])
async def process_hi1_command(message: types.Message):
    await message.reply(BotDB.get_records(32))


@dp.message_handler(commands=['hi3'])
async def process_hi1_command(message: types.Message):
    await message.reply(str1)


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
