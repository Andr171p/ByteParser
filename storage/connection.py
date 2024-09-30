from redis import Redis
from redis import asyncio as aioredis

from storage.logs import RedisLogs

from loguru import logger


class RedisConnection:
    _redis = None

    def __init__(self, url: str) -> None:
        self._url = url

    async def connect(self) -> Redis:
        self._redis = await aioredis.from_url(self._url)
        logger.info(RedisLogs.SUCCESSFULLY_CONNECT_LOG)
        return self._redis

    async def close(self) -> None:
        await self._redis.close()
        logger.info(RedisLogs.CLOSE_CONNECTION_LOG)
        # await cls._redis.wait_closed()
