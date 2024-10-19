import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards.reply import main_menu_kb
from bot.template_engine import engine
from bot.config import settings
from bot.states import GroupCreate
from service import group


group_router = Router()
logger = logging.getLogger(__name__)


@group_router.callback_query(F.data == "create_group")
async def create_group(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GroupCreate.name)  # установка состояния для получения имени
    await callback.message.answer(engine.render_template("create_group"))


@group_router.message(GroupCreate.name)
async def process_group_name(message: Message, state: FSMContext):
    # Проверка на имя

    # await state.update_data(name=message.text)  # сохранение имени
    await state.clear()

    group_id = await group.create_group(name=message.text, owner_id=message.from_user.id)
    await message.answer(engine.render_template(
        "group_created",
        group_name=message.text,
        group_id=group_id,
    ))


@group_router.callback_query(F.data == "join_group")
async def join_group(callback: CallbackQuery):
    await callback.message.answer("join_group")


@group_router.message(F.text.casefold() == "группа")
async def user_groups(message: Message, state: FSMContext):
    await message.answer("Твои группы:")
