import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8442255798:AAHJXdk7b12msH-j6rcwVfbXUniUHGx96po'
WEB_APP_URL = 'https://UzagroMaret.uz' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # Кнопка для открытия Web App
    kb = [
        [types.KeyboardButton(text="Открыть маркетплейс 🍎", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    
    await message.answer(
        "Добро пожаловать в агро-маркетплейс!\n"
        "Bozorimizga xush kelibsiz!", 
        reply_markup=keyboard
    )

@dp.message(lambda message: message.web_app_data)
async def handle_webapp_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Спасибо за заказ! Вы выбрали: {data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())