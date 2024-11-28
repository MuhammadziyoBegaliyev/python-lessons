from aiogram import Bot , Dispatcher, types ,F
from asyncio import run 
from lesson3 import get_user_info

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi!✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot to`xtatildi!❌")




async def start():
    dp.startup.register(startup_answer)
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    await dp.start_polling(bot, polling_timeout=1)








run(start())










