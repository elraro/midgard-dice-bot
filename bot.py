import telebot
import requests
import sys
import time
import urllib.parse

import telebot.types as types

bot = telebot.TeleBot("YOUR_TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    bot.send_message(cid, "Este bot es inline. Teclea su nombre en una conversación/grupo y podrás enviar la imagen de Midgard con el texto que has escrito.")


@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
    try:
        ##  '_.-'
        text = urllib.parse.quote_plus(inline_query.query).replace(".", "%2E").replace("_", "%5F").replace("-", "%2D")
        print("Texto: " + text + " id: " + inline_query.id)
        r = types.InlineQueryResultPhoto('1',
                                         'http://yourweb.com/image_generator/image.php?frase=' + text,
                                         'http://yourweb.com/image_generator/image.php?frase=' + text)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

while True:
    try:
        bot.polling(none_stop=True)
    except requests.exceptions.ConnectionError as e:
        print(sys.stderr, str(e))
        time.sleep(15)

