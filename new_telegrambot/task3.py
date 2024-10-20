from main import *
from task2 import * 
import telebot
import sqlite3

name = None

@bot.message_handler(commands=['ziyo'])
def ziyo(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXIST esers(id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Salom, biz sinzi ro`yhatdan o`tqazamiz! Ma`lumotlarni kiriting')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Parol kiriting')
    bot.register_next_step_handler(message, user_pass)




def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(f'INSERT INTO user (name, pass) VALUES ({name}, {password})')
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.typis.InlineKeyboarMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Foydalanuvchi ro`yhati', callback_data='user'))
    bot.send_message(message.chat.id, 'Ro`yhatdan o`tganlar', reply_markup=markup)
    # bot.send_message(message.chat.id, 'Parol kiriting')
    # bot.register_next_step_handler(message, user_pass)

bot.polling(none_stop=True)