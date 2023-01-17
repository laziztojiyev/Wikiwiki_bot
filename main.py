"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5885856640:AAHzwGOjPLAbtTBJr7XePuyT8P_cQ87hW60'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("o'zbekcha wikipediaga xush kelibsiz")


@dp.message_handler()
async def wiki_answer(message: types.Message):
    try:
        answer = wikipedia.summary(message.text)
        await message.answer(answer)
    except:
        await message.answer("bu so'z topilmadi")



#
#
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
