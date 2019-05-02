# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler
import os
from urllib.request import urlretrieve

# API-avain
token = os.environ['TGTORI_TOKEN']

def start(bot, update):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,
                    'Tervetuloa käyttämään Oulun Kauppatorin livekameran Telegram-bottia! Livefeedi löytyy Oulun kaupungin sivuilta osoitteesta https://www.ouka.fi/oulu/oulu-tietoa/nettikamerat')


def toripolliisi(bot, update):
    chat_id = update.message.chat.id
    urlretrieve("http://www.oulunkaupunki.fi/_private/kamera/picture1.jpg", "tori.jpg")
    bot.send_photo(chat_id, photo=open('tori.jpg', 'rb'))


updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('toripolliisi', toripolliisi))
updater.start_polling()
updater.idle()
