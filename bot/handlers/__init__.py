from aiogram import Dispatcher

from .common import common_router
from .test_states import form_router

def include_all_routers(dp: Dispatcher) -> None:
    """
    Подключение всех роутеров к диспетчеру
    """
    dp.include_router(common_router)
    dp.include_router(form_router)
