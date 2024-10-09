from aiogram import Dispatcher

from .commands import commands_router

def include_all_routers(dp: Dispatcher) -> None:
    """
    Подключение всех роутеров к диспетчеру
    """
    dp.include_router(commands_router)
