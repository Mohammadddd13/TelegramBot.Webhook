import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = "8357943292:AAFj1-EqFaYcJv0v3i5oaiAq0PukEY8RHgo"

# تعریف تابع استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 DARKLEGENDSIR", url="https://t.me/DARKLEGENDSIR")],
        [InlineKeyboardButton("⚡ DARK LEGENDS CHANNEL", url="https://t.me/DARK_LEGENDS_CHANNEL")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"✅ سلام {update.effective_user.full_name}! خوش آمدی 🎉\nنیازی به عضویت در کانال‌ها نیست، فقط می‌تونی نگاه کنی.",
        reply_markup=reply_markup
    )

# ایجاد اپلیکیشن ربات
async def main():
    app = ApplicationBuilder().token(API_TOKEN).build()
    
    # اضافه کردن Command Handler
    app.add_handler(CommandHandler("start", start))
    
    # شروع ربات
    await app.start()
    await app.updater.start_polling()
    await app.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
