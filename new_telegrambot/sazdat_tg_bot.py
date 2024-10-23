# from tok import  key, apiKey 
from aiogram import Bot, Dispatcher, executor, types
import requests
import json

        
bot = Bot('7919107569:AAFhxTZuLhmW7iFLIKwKbxznm28Vy-XCPno')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def info(message:types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('ob-havo malumotlari!',callback_data='city'))
    markup.add(types.InlineKeyboardButton('kamandani kiriting',callback_data='list'))
    await message.reply('Salom, Bu yerda ob-havo ma`lumotlarini bilib olishingiz mumkun', reply_markup=markup)


@dp.message_handler(commands=['listCity'])
async def reply(message:types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton('Andijon'))
    markup.add(types.InlineKeyboardButton('Namangan'))
    markup.add(types.InlineKeyboardButton('Fargona'))
    markup.add(types.InlineKeyboardButton('Toshkent'))
    markup.add(types.InlineKeyboardButton('Buxoro'))
    markup.add(types.InlineKeyboardButton('Jizzax'))
    markup.add(types.InlineKeyboardButton('Zarafshon'))
    markup.add(types.InlineKeyboardButton('Navoiy'))
    markup.add(types.InlineKeyboardButton('Qarshi'))
    markup.add(types.InlineKeyboardButton('Samarqand'))
    markup.add(types.InlineKeyboardButton('Nukus'))
    markup.add(types.InlineKeyboardButton('Termiz'))
    markup.add(types.InlineKeyboardButton('Urganch'))
    markup.add(types.InlineKeyboardButton('Xiva'))
    markup.add(types.InlineKeyboardButton('Guliston'))
    await message.reply('Salom', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    if call.data == 'list':
        await call.message.answer('/listCity\n/start')
    elif call.data == 'city':
        await call.message.answer('Shaxar kirit :')

@dp.message_handler(content_types=['text'])
async def reply(message:types.Message):
    city = message.text.lower().strip()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metri'
    res = requests.get(url)
    data = json.loads(res.text)
    if res.status_code==200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

    elif res.status_code == 404:
        await message.reply(f"Shaxar topilmadi ")




executor.start_polling(dp)