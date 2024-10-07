import logging

from aiogram import Dispatcher, Router, F
from aiogram.filters import Command, Filter
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

common_router = Router()
logger = logging.getLogger(__name__)

class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


@common_router.message(Command("start"))
async def start_handler(message: Message) -> None:
    logger.debug(f"Sent answer to /start command. To user {message.from_user.username}")
    await message.answer("hello world!")


@common_router.message(MyFilter("hello"))
async def hello_handler(message: Message) -> None:
    logger.debug(f"Sent answer to <hello>. To user {message.from_user.username}")
    await message.answer("hi")


@common_router.message(F.text.regexp(r"^(\d+)$"))
async def any_digits_handler(message: Message) -> None:
    logger.debug(f"Sent answer to digit message. To user {message.from_user.username}")
    await message.answer("This is digits!")
