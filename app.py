import asyncio
import logging
import os
import sys
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.routers import include_all_routers
from bot.config import settings


VERSION = "1.0.8"
load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)


async def main():
    logging.getLogger("aiogram").setLevel("WARNING")
    logging.getLogger("asyncio").setLevel("INFO")
    # logging.basicConfig(filename=f"logs/bot_logs_{datetime.datetime.now().strftime('%Y_%m_%d')}.log",
    #                     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level="DEBUG",
    #                     datefmt="%Y-%m-%d %H:%M:%S", filemode='a')
    logging.basicConfig(
        format=settings.logging.format,
        datefmt=settings.logging.datefmt,
        level="DEBUG" if settings.logging.debug else "INFO",
        stream=sys.stdout)

    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)  # пропуск сообщения пока бот был оффлайн

    dp = Dispatcher()
    include_all_routers(dp)  # подключение роутеров


    logger.info("Start polling...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
