import telebot
import datetime
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0 <= current_time.hour < 6:
        return 'Доброй ночи!'
    if 6 <= current_time.hour < 12:
        return 'Доброе утро!'
    if 12 <= current_time.hour < 17:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Какой фильм тебя интересует?\n\n' \
    f'Список команд:\n' \
    f'/choose_genre - выбрать жанр\n' \
    f'/choose_year - выбрать год\n' \
    f'/choose_film - случайный выбор\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['choose_film'])
def choose_film(message: telebot.types.Message):
    with open('films1_txt', 'r', encoding='utf-8') as file:
        films = file.read().split('\n')
    film = random.choice(films)
    bot.send_message(message.chat.id, text=f'Сегодня вечером стоит посмотреть "{film}"')

@bot.message_handler(commands=['choose_genre'])
def choose_genre(message: telebot.types.Message):
    text = f'Список жанров:\n' \
    f'/horror - ужасы\n' \
    f'/comedy - комедия\n' \
    f'/detective - детектив\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['horror'])
def horror(message: telebot.types.Message):
    with open('horrors', 'r', encoding='utf-8') as file:
        horrors=file.read()
    bot.send_message(message.chat.id, text=f'Ужасы:\n{horrors}\n')

@bot.message_handler(commands=['comedy'])
def comedy(message: telebot.types.Message):
    with open('comedies', 'r', encoding='utf-8') as file:
        comedies=file.read()
    bot.send_message(message.chat.id, text=f'Комедии:\n{comedies}\n')

@bot.message_handler(commands=['detective'])
def detective(message: telebot.types.Message):
    with open('detectives', 'r', encoding='utf-8') as file:
        detectives=file.read()
    bot.send_message(message.chat.id, text=f'Детективы:\n{detectives}\n')

@bot.message_handler(commands=['choose_year'])
def choose_year(message: telebot.types.Message):
    text = f'Дата выхода фильма:\n' \
    f'/nineties - 1990-1999\n' \
    f'/zeros - 2000-2009\n' \
    f'/tens - 2010-2019\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['nineties'])
def nineties(message: telebot.types.Message):
    with open('nineties', 'r', encoding='utf-8') as file:
        nineties= file.read()
    bot.send_message(message.chat.id, text=f'1990-1999:\n{nineties}')

@bot.message_handler(commands=['zeros'])
def zeros(message: telebot.types.Message):
    with open('zeros', 'r', encoding='utf-8') as file:
        zeros= file.read()
    bot.send_message(message.chat.id, text=f'2000-2009:\n{zeros}')

@bot.message_handler(commands=['tens'])
def tens(message: telebot.types.Message):
    with open('tens', 'r', encoding='utf-8') as file:
        tens= file.read()
    bot.send_message(message.chat.id, text=f'2010-2019:\n{tens}')

@bot.message_handler(func=lambda _: True)
def unknown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неизвестная команда')

bot.infinity_polling()
