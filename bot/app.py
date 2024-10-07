import asyncio
import logging
import os
import sys
import datetime

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv, find_dotenv
from handlers import include_all_routers


VERSION = "1.0.3"
load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)


async def main():
    logging.getLogger("aiogram").setLevel("WARNING")
    logging.getLogger("asyncio").setLevel("INFO")
    # logging.basicConfig(filename=f"logs/bot_logs_{datetime.datetime.now().strftime('%Y_%m_%d')}.log",
    #                     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level="DEBUG",
    #                     datefmt="%Y-%m-%d %H:%M:%S", filemode='a')
    logging.basicConfig(level="DEBUG", stream=sys.stdout)

    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    include_all_routers(dp)  # подключение роутеров

    logger.info("Start polling...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
