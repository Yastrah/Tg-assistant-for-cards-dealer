from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def join_create_room() -> InlineKeyboardMarkup:
    """
    Клавиатура для вступления/создания группы
    """
    kb = InlineKeyboardBuilder()
    # kb.row(InlineKeyboardButton(
    #     text="создать группу", callback_data='create_group')
    # )
    kb.button(text="создать комнату", callback_data='create_room')
    kb.button(text="зайти в комнату", callback_data='join_room')
    kb.adjust(1)
    return kb.as_markup()
