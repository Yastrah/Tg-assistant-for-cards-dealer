from typing import Any, Dict

from aiogram import Router, F, html
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,  # чистка клавиатуры
)

# class Form(StatesGroup):
#     name = State()
#     like_bots = State()
#     language = State()


# название конкретного состояние соответствует ожидаемому ответу при этом состоянии
class GroupCreate(StatesGroup):
    name = State()


