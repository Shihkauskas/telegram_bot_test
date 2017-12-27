# -*- coding: utf-8 -*-

import base64
import time
import datetime
import config
import telebot
from telebot import types
import openWeather
from habra import habr_news

key_t = base64.b64decode(config.token).decode()
bot = telebot.TeleBot(key_t)
main_commands = {'/start': 'тестовое приветствие или просто используй "привет"',
                 '/help': 'Вывод доступных команд',
                 '/news': 'новости питона с хабры',
                 '/weather': 'текущая погода в Челябинске',
                 '/channel': 'отправка в канал'
                 }


def send_to_channel():
    while True:
        bot.send_message(config.channel_name, 'TEEEEST')
        time.sleep(20)


@bot.message_handler(func=lambda message: message.text == "привет")
def greeting(message):
    now = datetime.datetime.now().hour
    if 6 <= now <= 12:
        bot.send_message(message.chat.id, 'Доброе утро\n Для подробной справки воспользуйтесь /help')
    elif 12 < now < 17:
        bot.send_message(message.chat.id, 'Добрый день\n Для подробной справки воспользуйтесь /help')
    else:
        bot.send_message(message.chat.id, 'Добрый вечер\n Для подробной справки воспользуйтесь /help')


@bot.message_handler(commands=['channel'])
def send_to_channel(message):
    bot.send_message(config.channel_name, 'тестовое сообщение ' + str(datetime.datetime.now()))


@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in main_commands.keys()])
    bot.send_message(message.chat.id, 'Выбери',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    help_text = 'Команды для выполнения:\n'
    for key in main_commands:
        help_text += key + ': '
        help_text += main_commands[key] + '\n'
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['news'])
def news(message):
    last_new = habr_news()
    if len(last_new) != 0:
        for i in last_new:
            bot.send_message(message.chat.id, i)
            time.sleep(1)
    else:
        bot.send_message(message.chat.id, 'Новых новостей нет')


@bot.message_handler(commands=['weather'])
def news(message):
    bot.send_message(message.chat.id, openWeather.weather())
    bot.send_message(message.chat.id, openWeather.forecast())


@bot.message_handler(content_types=['text'])
def defuaul_text(message):
    bot.send_message(message.chat.id, 'Не пиши "{}" здесь, лучше попробуй /start'.format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
