import telebot 
import random


TOKEN = '7629446596:AAEDJHMss-7smOHqno-pMlDn_XFAvpYgWQg' # bot tokenini kiritamiza 
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    xabar = f"Assalomu aleykum {username} O`zbekiston mintaqasi bo`yicha ob-havo botiga hush kelib siz😊!"
    xabar += '\nShaxar kiriting 🌤'
    bot.reply_to(message, xabar)

@bot.message_handler(func=lambda msg: msg.text is not None)
def tallash(message):
    msg = message.text
    tasodifiy_son = random.randint(0,50)
    bot.reply_to(message, f"Hozirgi harorat: {tasodifiy_son}°C")  


bot.polling()

