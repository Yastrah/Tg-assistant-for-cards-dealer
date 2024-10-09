import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.keyboards.reply import main_menu_kb
from bot.template_engine import engine
from bot.config import settings


group_router = Router()
logger = logging.getLogger(__name__)


@group_router.callback_query(F.data == "create_group")
async def create_group(callback: CallbackQuery):
    await callback.message.answer("create_group")


@group_router.callback_query(F.data == "join_group")
async def join_group(callback: CallbackQuery):
    await callback.message.answer("join_group")