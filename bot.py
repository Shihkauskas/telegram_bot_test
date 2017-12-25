# -*- coding: utf-8 -*-

import base64
import time
import datetime
import config
import telebot
import openWeather
from habra import habr_news

key = base64.b64decode(config.token).decode()
bot = telebot.TeleBot(key)
main_commands = {'start': 'Приветсвие',
                 'help': 'Вывод доступных команд',
                 'news': 'новости питона с хабры',
                 'weather': 'текущая погода в Челябинске'
}

@bot.message_handler(commands=['start'])
def command_start(message):
    now = datetime.datetime.now().hour
    if 6 <= now <= 12:
        bot.send_message(message.chat.id, 'Доброе утро\n Для подробной справки воспользуйтесь /help')
    elif 12 < now < 17:
        bot.send_message(message.chat.id, 'Добрый день\n Для подробной справки воспользуйтесь /help')
    else:
        bot.send_message(message.chat.id, 'Добрый вечер\n Для подробной справки воспользуйтесь /help')


@bot.message_handler(commands=['help'])
def help(message):
    help_text = 'Команды для выполнения:\n'
    for key in main_commands:
        help_text += '/' + key + ': '
        help_text += main_commands[key] + '\n'
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['news'])
def news(message):
    for i in habr_news():
        bot.send_message(message.chat.id, i)
        time.sleep(1)


@bot.message_handler(commands=['weather'])
def news(message):
    bot.send_message(message.chat.id, openWeather.weather())
    bot.send_message(message.chat.id, openWeather.forecast())


@bot.message_handler(content_types=['text'])
def defuaul_text(message):
    bot.send_message(message.chat.id, 'Не пиши "{}" здесь, лучше попробуй /help'.format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
