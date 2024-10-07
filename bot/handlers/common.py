import logging

from aiogram import Dispatcher, Router, F
from aiogram.filters import Command, Filter
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()
logger = logging.getLogger(__name__)

class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


async def start_handler(message: Message) -> None:
    logger.debug(f"Sent answer to /start command. To user {message.from_user.username}")
    await message.answer("hello world!")


async def hello_handler(message: Message) -> None:
    logger.debug(f"Sent answer to <hello>. To user {message.from_user.username}")
    await message.answer("hi")


async def any_digits_handler(message: Message) -> None:
    logger.debug(f"Sent answer to digit message. To user {message.from_user.username}")
    await message.answer("This is digits!")


# router.message.register(my_handler, Command("my_command"), MyFilter())
def register_handlers_common(dp: Dispatcher):
    router.message.register(start_handler, Command("start"))
    router.message.register(hello_handler, MyFilter("hello"))
    router.message.register(any_digits_handler, F.text.regexp(r"^(\d+)$"))
    # dp.register_message_handler(cmd_start, commands="start", state="*")

    dp.include_router(router)