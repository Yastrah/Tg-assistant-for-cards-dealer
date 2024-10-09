import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.keyboards.reply import main_menu_kb
from bot.template_engine import engine
from bot.config import settings


commands_router = Router()
logger = logging.getLogger(__name__)


@commands_router.message(Command("start"))
@commands_router.message(F.text.casefold() == "start")
async def start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(engine.render_template(
        "start",
        user_name=message.from_user.username,
        bot_name=settings.bot.name
    ),
        reply_markup=main_menu_kb())
    logger.debug(f"Sent answer to /start command. To user {message.from_user.username}")

