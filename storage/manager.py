from redis import Redis

from storage.connection import RedisConnection

from loguru import logger


class RedisManager(RedisConnection):
    @staticmethod
    async def keys(redis: Redis) -> list:
        keys = await redis.keys('*')
        return keys

    @classmethod
    async def clear(cls) -> None:
        redis = await cls.connect()
        keys = await cls.keys(redis=redis)
        try:
            await redis.delete(*keys)
        except Exception as _ex:
            logger.warning(_ex)
        finally:
            await cls.close()

