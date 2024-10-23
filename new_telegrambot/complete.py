import telebot
import requests
import json


bot = telebot.TeleBot('7919107569:AAFhxTZuLhmW7iFLIKwKbxznm28Vy-XCPno')
API ='7e807ceda95d136880e1f6a29e64f3cf'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Salom , Istalgan shaxaringizni kiriting :')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"Hozirgi ob-havo:{temp}")
    else:
        bot.reply_to(message, f"bundey shaxar topilmadi ")

    image = 'sun.png' if temp > 280.0  else 'cloud.png'
    file = open('./'+image, 'r')
    bot.send_photo(message.chat.id, file)





bot.polling(none_stop=True)