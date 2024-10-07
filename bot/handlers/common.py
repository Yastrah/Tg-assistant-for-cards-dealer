import logging

from aiogram import Router, F
from aiogram.filters import Command, Filter
from aiogram.types import (
    Message,
)

from bot.template_engine import engine

common_router = Router()
logger = logging.getLogger(__name__)

class MyFilter(Filter):
    """
    Собственный фильтр в котором можно обработать всё необходимое
    """
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:  # вызывается роутером для проверки соответствия
        return message.text == self.my_text


@common_router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(engine.render_template(
        "start",
        user_name=message.from_user.first_name,
        bot_name="Bot"
    ))
    logger.debug(f"Sent answer to /start command. To user {message.from_user.username}")


@common_router.message(MyFilter("hello"))
async def hello_handler(message: Message) -> None:
    await message.answer("hi")
    logger.debug(f"Sent answer to <hello>. To user {message.from_user.username}")


@common_router.message(F.text.regexp(r"^(\d+)$"))
async def any_digits_handler(message: Message) -> None:
    await message.answer("This is digits!")
    logger.debug(f"Sent answer to digit message. To user {message.from_user.username}")
