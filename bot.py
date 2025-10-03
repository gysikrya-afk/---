import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher
from app.heandler import router

async def main():
    load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')
    bot = Bot(TOKEN)
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
