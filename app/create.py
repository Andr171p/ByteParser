from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot.config import BotToken
from app.bot.handlers.start import start_router
from app.bot.handlers.username import username_router
from app.bot.handlers.values import values_router


bot = Bot(
    token=BotToken().TOKEN,
    parse_mode=ParseMode.HTML
)

dp = Dispatcher(
    storage=MemoryStorage()
)

dp.include_routers(
    start_router,
    username_router,
    values_router
)
