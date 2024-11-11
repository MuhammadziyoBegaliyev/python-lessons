import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('7629446596:AAEDJHMss-7smOHqno-pMlDn_XFAvpYgWQg')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Salom! Istalgan shahar nomini k  iriting!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    url = f'https://obhavo.uz/{city}'  # Shahar nomi bilan URLni yangilang
    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Ma'lumotlarni olish (saytdagi HTML strukturasiga mos ravishda)
        try:
            temp = soup.find('span', class_='current-temperature').text.strip()  # Bu yerda klass nomini to'g'rilash
            description = soup.find('div', class_='weather-description').text.strip()  # Bu yerda klass nomini to'g'rilash
            
            bot.reply_to(message, f'Hozirgi ob-havo: {temp}°C\nHavo: {description}')
        except AttributeError:
            bot.reply_to(message, "Ob-havo ma'lumotlarini olishda xato. Iltimos, to'g'ri shahar nomini kiriting.")
    else:
        bot.reply_to(message, "Shahar topilmadi. Iltimos, to'g'ri shahar nomini kiriting.")

bot.polling(none_stop=True)
