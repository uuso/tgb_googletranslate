import os
import sys
import telebot
from googletrans import Translator


translator = Translator()
bot = telebot.TeleBot(os.getenv('TOKEN') or sys.argv[1])
lang = {'en', 'ru'}

@bot.message_handler(commands=['start', 'help'])
def greet(message):
    text = 'Привет'
    bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')

# обработка любого необработанного текстового сообщения
@bot.message_handler()
def log_all(message):
    text = message.text
    lang_detected = translator.detect(text).lang

    lang_src = lang_detected if lang_detected in lang else 'en'
    lang_dst = lang - {lang_src}
    lang_dst = lang_dst.pop()

    response = translator.translate(text, src=lang_src, dest=lang_dst).text
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


bot.infinity_polling()