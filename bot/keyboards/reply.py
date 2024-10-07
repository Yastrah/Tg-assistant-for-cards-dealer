from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Yes")
    kb.button(text="No")
    kb.adjust(2)
    # kb.adjust(3, 2)  # в первой строке 3 кнопки, во второй 2
    return kb.as_markup(resize_keyboard=True)  # resize чтобы сделать кнопки пропорциональными
