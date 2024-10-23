import telebot
from tok import key
from telebot import types
import webbrowser


bot = telebot.TeleBot(key)
@bot.message_handler(commands=['start'])
def start(message):
    mark = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Maktab web saxifasiga o`ting.')
    mark.row(btn1)
    btn2 = types.KeyboardButton('O`chirish')
    btn3 = types.KeyboardButton('Taxrirlash')
    mark.row(btn2,btn3)
    bot.send_message(message.chat.id,'Salom',reply_markup=mark)

bot.polling()