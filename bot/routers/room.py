import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards.reply import main_menu_kb
from bot.template_engine import engine
from bot.config import settings
from bot.states import RoomCreate, RoomJoin
from service import room


room_router = Router()
logger = logging.getLogger(__name__)


@room_router.callback_query(F.data == "create_room")
async def create_room(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RoomCreate.get_name)  # установка состояния для получения имени
    await callback.message.answer(engine.render_template("create_room"))


@room_router.message(RoomCreate.get_name)
async def process_room_get_name(message: Message, state: FSMContext):
    # Проверка на имя

    # await state.update_data(name=message.text)  # сохранение имени
    await state.clear()

    group_id = await room.create_room(name=message.text, owner_id=message.from_user.id)
    await message.answer(engine.render_template(
        "room_created",
        room_name=message.text,
        room_id=group_id,
    ))


@room_router.callback_query(F.data == "join_room")
async def join_room(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RoomCreate.get_name)

    await callback.message.answer("Введите id группы")


@room_router.message(RoomJoin.get_id)
async def process_room_get_id(message: Message, state: FSMContext):
    await state.clear()

    


@room_router.message(F.text.casefold() == "группа")
async def user_rooms(message: Message, state: FSMContext):
    await message.answer("Твои группы:")
