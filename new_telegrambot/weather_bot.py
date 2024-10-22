import telebot
import requests
import json

bot = telebot.TeleBot('7843936213:AAERyf2jk-oAypnim4bIqMB3Kch5agz-_pQ')
API = '7e807ceda95d136880e1f6a29e64f3cf'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Salom , Istalgan shaxar nomini kiriting!')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'Hozirgi ob-havo: {temp}')

    image = 'image.png' if temp >5.0 else 'image copy.png'
    file = open('./.'+image, 'rb')
    bot.send_photo(message.chat.id, file)

bot.polling(none_stop=True)