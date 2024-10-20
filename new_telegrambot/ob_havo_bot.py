from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import asyncio
import requests

TOKEN = "7843936213:AAERyf2jk-oAypnim4bIqMB3Kch5agz-_pQ"
bot= Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Salom! Ob-havo haqida bilmoqchimisiz? Marhamat shaxarni kiriting.')


@dp.message(F.text)
async def get_weather(message: types.Message):
    city = message.text
    try:
        url = f"https://obhavo.uz/"
        weather_data = requests.get(url).json()
        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        cloud_cover = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']


        await message.answer(f'Havo harorati: {temperature}°C\n'
                             f'Ajoyiblik:{temperature_feels}°C\n)'
                             f'Shamol:{wind_speed}m/s\n'
                             f'Bulutlilik:{cloud_cover}\n'
                             f'Namlik:{humidity}%')
    except KeyError:
        await message.answer(f'Shaxarni aniqlab bo`lmadi:{city}')

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())