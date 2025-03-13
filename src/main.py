from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from asyncio import run
import logging
import sys
from handlers.start_handler import router

load_dotenv()

BOT_TOKEN = getenv("TG_TOKEN")
if not BOT_TOKEN:
    raise ValueError("TG_TOKEN is not set in .env file")

db = Dispatcher()

db.include_router(router=router)

async def main():
    bot = Bot(
        token = BOT_TOKEN
    )
    logging.info("Bot start work")
    await db.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(main())