import telebot
import webbrowser


bot = telebot.TeleBot('7234776184:AAG3WlpA_8Se8HlZrymT-0t2YUb9BJuRkKU')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://obhavo.uz')


@bot.message_handler(commands=['start' ])
def main(message):
    if None != message.from_user.last_name :
        bot.send_message(message.chat.id, f"Salom, {message.from_user.first_name} {message.from_user.last_name}")
    else:
        bot.send_message(message.chat.id, f"Salom, {message.from_user.first_name}")


@bot.message_handler(commands=['tel_number'])
def main(message):
    bot.send_message(message.chat.id, '901431051')


@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, 'Adminga murojat qilish :@Muhammadziyo090')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Muhammadziyodan sizga alangalik salomlar!</b> <em><u>Menga murojat qilin :901431051</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == "salom":
        bot.send_message(message.chat.id, f"Salom, {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')




