import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name 
    user_id = message.from_user.id
    text = f'Привет, {user_name}'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


