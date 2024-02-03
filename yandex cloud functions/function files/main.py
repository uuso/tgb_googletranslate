import os
import telebot
from googletrans import Translator

def has_cyrillic(text) -> bool:
    """Checks if there are any cyrillic symbols in TEXT.
Cyrillic symbols are doublesized.
"""
    return len(text.encode("utf-8", "ignore")) > len (text)

bot = telebot.TeleBot(os.getenv('TOKEN'))
    
translator = Translator()

@bot.message_handler(commands=['start', 'help'])
def greet(message):
    text = 'Привет'
    bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')

# обработка любого необработанного текстового сообщения
@bot.message_handler()
def log_all(message):
    text = message.text.replace('’', "'")
    lang_src, lang_dst = ('ru', 'en') if has_cyrillic(text) else ('en', 'ru')
    response = translator.translate(
                                    text, 
                                    src=lang_src, 
                                    dest=lang_dst
        ).text
    bot.send_message(message.chat.id, f'`{response}`', parse_mode='MarkdownV2')

if __name__ == '__main__':
    # local tests
    bot.infinity_polling()