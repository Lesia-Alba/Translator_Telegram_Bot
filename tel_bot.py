import logging
import os
import re

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO,
    filename="bot.log",
    format="%(asctime)s %(levelname)s %(message)s"
)

letters = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
    "Е": "E", "Ё": "E", "Ж": "Zh", "З": "Z", "И": "I",
    "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N",
    "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Ts", "Ч": "Ch",
    "Ш": "Sh", "Щ": "Shch", "Ы": "Y", "Ъ": "IE", "Э": "E", "Ю": "IU", "Я": "IA", 'Ь':''
}

def translate(text: str) -> str:
    result = []
    for el in text:
        upper_el = el.upper()
        if upper_el in letters:
            result.append(letters[upper_el])
        else:
            result.append(el)
    new_name = ''.join(result)
    return new_name.title()
   
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name 
    user_id = message.from_user.id
    text = f'Привет, {user_name}, пожалуйста напиши свое ФИО на кирилице и я переведу его на латиницу.'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def translate_fio(message: Message):
    user_name = message.from_user.full_name 
        
    text = message.text.strip()
    if not re.fullmatch(r"[А-Яа-яЁё\s\-]+", text):
        text = f'{user_name}, пожалуйста напиши свое ФИО на кирилице без цифр и латинских букв'
        await message.answer(text=text)
        return

    translation = translate(text)
    logging.info(f'Получено ФИО:{text}, перевод: {translation}')
    await message.answer(f"Твое ФИО латиницей: {translation}")
    
if __name__ == '__main__':
    dp.run_polling(bot)


