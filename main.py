import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# BotFather'dan olgan tokeningizni shu yerga yozasiz
8520121471:AAG98HAXbs_bR-tmy4AG9G6Hq8-MldbeJyQ

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Menga Instagram yoki TikTok havolasini yuboring, men sizga videoni yuklab beraman! 🚀")

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text
    if "instagram.com" in url or "tiktok.com" in url:
        await message.reply("⏳ Video yuklab olinmoqda, biroz kuting...")
        # Bu yerda video yuklash amali bajariladi
    else:
        await message.reply("Iltimos, faqat Instagram yoki TikTok havolasini yuboring!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)8520121471:AAG98HAXbs_bR-tmy4AG9G6Hq8-MldbeJyQ
