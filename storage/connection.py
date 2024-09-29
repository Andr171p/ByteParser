from redis import Redis
from redis import asyncio as aioredis

from storage.settings import RedisSettings
from storage.logs import RedisLogs

from loguru import logger


class RedisConnection:
    _redis = None

    @classmethod
    async def connect(cls) -> Redis:
        cls._redis = await aioredis.from_url(RedisSettings.PUBLIC_URL)
        logger.info(RedisLogs.SUCCESSFULLY_CONNECT_LOG)
        return cls._redis

    @classmethod
    async def close(cls) -> None:
        await cls._redis.close()
        logger.info(RedisLogs.CLOSE_CONNECTION_LOG)
        # await cls._redis.wait_closed()
