from redis import Redis

from storage.connection import RedisConnection
from storage.logs import RedisLogs

from loguru import logger


class RedisManager(RedisConnection):
    @staticmethod
    async def keys(redis: Redis) -> list:
        keys = await redis.keys('*')
        return keys

    async def delete(self, key: str | int) -> None:
        redis = await self.connect()
        key = str(key)
        try:
            await redis.delete(key)
            logger.info(RedisLogs.SUCCESSFULLY_DELETE_LOG.format(keys=key))
        except Exception as _ex:
            logger.warning(_ex)
        finally:
            await self.close()

    async def clear(self) -> None:
        redis = await self.connect()
        keys = await self.keys(redis=redis)
        try:
            await redis.delete(*keys)
            logger.info(RedisLogs.SUCCESSFULLY_DELETE_LOG.format(keys=keys))
        except Exception as _ex:
            logger.warning(_ex)
        finally:
            await self.close()
