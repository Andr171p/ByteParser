import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot.config import BotToken
from app.bot.handlers.start import start_router
from app.bot.handlers.username import username_router
from app.bot.handlers.values import values_router

from service.scheduler import Scheduler
from service.tasks import task
from service.settings import ServiceSettings

from misc.utils import calculate_timeout


bot = Bot(token=BotToken().TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(
    start_router,
    username_router,
    values_router
)


async def telegram_bot() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def values_rate() -> None:
    timeout = calculate_timeout(
        hour=ServiceSettings.HOUR,
        minute=ServiceSettings.MINUTE,
        second=ServiceSettings.SECOND,
        microsecond=ServiceSettings.MICROSECOND
    )
    scheduler = Scheduler(
        timeout=timeout,
        task=task
    )
    await scheduler.scheduler()


async def main() -> None:
    await asyncio.gather(
        telegram_bot(),
        values_rate()
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
