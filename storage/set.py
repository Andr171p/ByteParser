from storage.connection import RedisConnection
from storage.logs import RedisLogs

from misc.utils import timestamp

from loguru import logger


class RedisSetValues(RedisConnection):
    async def set(
            self, key: str, usd: float, eur: float, gbp: float
    ) -> None:
        redis = await self.connect()
        await redis.hset(
            name=key,
            mapping={
                'usd': usd,
                'eur': eur,
                'gbp': gbp,
                'timestamp': timestamp()
            }
        )
        logger.info(RedisLogs.SUCCESSFULLY_SET_LOG)
        await self.close()


class RedisSetUser(RedisConnection):
    async def set(self, key: int | str, username: str) -> None:
        redis = await self.connect()
        await redis.hset(
            name=str(key),
            mapping={
                'username': username,
                'timestamp': timestamp()
            }
        )
        logger.info(RedisLogs.SUCCESSFULLY_SET_LOG)
        await self.close()
