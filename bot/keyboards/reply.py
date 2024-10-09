from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_no_kb() -> ReplyKeyboardMarkup:
    """
    Клавиатура с кнопками Да и Нет
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Yes")
    kb.button(text="No")
    kb.adjust(2)
    # kb.adjust(3, 2)  # в первой строке 3 кнопки, во второй 2
    return kb.as_markup(resize_keyboard=True)  # resize чтобы сделать кнопки пропорциональными


def main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Клавиатура главного меню(основная)
    """
    kb = ReplyKeyboardBuilder()
    # write
    return kb.as_markup(resize_keyboard=True)
