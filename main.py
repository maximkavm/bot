import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()

# Загружаем список поговорок
f = open('data/telefon.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot('5104763927:AAEc4bkq7nWqVKzeXOu-YF_Z5SjotTZn_7w')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        item3 = types.KeyboardButton("Телефоны")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка1':
            answer = random.choice(thinks)
    elif message.text.strip() == 'Телефоны':
            answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
