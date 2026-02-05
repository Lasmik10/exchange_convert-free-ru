from aiogram import Dispatcher

from handlers.start import router as router_start
from handlers.help import router as router_help
from handlers.list import router as router_list
from handlers.convert import router as router_convert


def register_routers(dp: Dispatcher):
    
    dp.include_router(router_start)
    dp.include_router(router_help)
    dp.include_router(router_list)
    dp.include_router(router_convert)