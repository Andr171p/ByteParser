import asyncio

from loguru import logger

from service.logs import ServiceLogs


class Scheduler:
    def __init__(self, timeout: int, task: callable) -> None:
        self._timeout = timeout
        self._task = task

    async def scheduler(self) -> None:
        logger.info(ServiceLogs.START_SERVICE_LOG)
        await self._task()
        while True:
            await asyncio.sleep(self._timeout)
            await self._task()
