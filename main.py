import random

from aiogram.dispatcher.filters import Command

from db import BotDB
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

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

# Объект бота
bot = Bot(token="5104763927:AAEc4bkq7nWqVKzeXOu-YF_Z5SjotTZn_7w")

# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')
button_tf = KeyboardButton('Телефонная книга')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
greet_kb.add(button_tf)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(nt(facts), reply_markup=greet_kb)


@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb)


@dp.message_handler(commands=['hi2'])
async def process_hi1_command(message: types.Message):
    await message.reply(BotDB.get_records(32))


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

# Запускаем бота
# bot.polling(none_stop=True, interval=0)
