from storage.connection import RedisConnection
from storage.logs import RedisLogs

from loguru import logger


class RedisSet(RedisConnection):
    @classmethod
    async def set(
            cls, key: str, usd: float, eur: float, gbp: float, timestamp: int
    ) -> None:
        redis = await cls.connect()
        await redis.hset(
            name=key,
            mapping={
                'usd': usd,
                'eur': eur,
                'gbp': gbp,
                'timestamp': timestamp
            }
        )
        logger.info(RedisLogs.SUCCESSFULLY_SET_LOG)
        await cls.close()


redis_set = RedisSet()
