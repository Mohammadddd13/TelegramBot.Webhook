import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = "8357943292:AAFj1-EqFaYcJv0v3i5oaiAq0PukEY8RHgo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="📢 DARKLEGENDSIR", url="https://t.me/DARKLEGENDSIR")],
            [types.InlineKeyboardButton(text="⚡ DARK LEGENDS CHANNEL", url="https://t.me/DARK_LEGENDS_CHANNEL")]
        ]
    )
    
    await message.answer(
        f"✅ سلام {message.from_user.full_name}! خوش آمدی 🎉\nنیازی به عضویت در کانال‌ها نیست، فقط می‌تونی نگاه کنی.",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
