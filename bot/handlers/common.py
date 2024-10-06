import logging

from aiogram import Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()

@router.message()
async def start_handler(message: Message, state: FSMContext) -> None:
    await message.answer("hello world!")


def register_handlers_common(dp: Dispatcher):
    # dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.include_router(router)