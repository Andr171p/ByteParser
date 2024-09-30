import asyncio
import logging

from app.create import (
    bot,
    dp
)

from service.scheduler import Scheduler
from service.tasks import task
from service.settings import ServiceSettings

from misc.utils import calculate_timeout


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
