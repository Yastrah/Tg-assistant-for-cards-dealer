from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def join_create_group() -> InlineKeyboardMarkup:
    """
    Клавиатура для вступления/создания группы
    """
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(
        text="создать группу", callback_data='create_group')
    )
    kb.row(InlineKeyboardButton(
        text="вступить в группу", callback_data='join_group')
    )
    return kb.as_markup()
