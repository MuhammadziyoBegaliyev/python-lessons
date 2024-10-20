from main import *
from telebot import types

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    bat1=types.InlineKeyboardButton('Saytga o`ting', url='https://obhavo.uz')
    markup.row(bat1)
    bat2=types.InlineKeyboardButton('Rasmni o`chirish', callback_data='delete')
    bat3=types.InlineKeyboardButton('Matn kiriting', callback_data='edit')
    markup.row(bat3,bat2)
    bot.reply_to(message, 'Qandey chiroyli rasm!💋', reply_markup=markup)


@bot.callback_query_handler(func = lambda callback : True)
def callback_message(callback) :
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)