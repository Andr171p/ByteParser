from redis import Redis

from storage.connection import RedisConnection
from storage.logs import RedisLogs
from storage.structure import (
    RedisValuesStructure,
    RedisUserStructure
)

from loguru import logger

from typing import List


class RedisGetValues(RedisConnection):
    @staticmethod
    async def keys(redis: Redis) -> list:
        keys = await redis.keys('*')
        logger.info(RedisLogs.KEYS_LOG.format(keys=keys))
        return keys

    @staticmethod
    async def zipped(redis: Redis, keys: list) -> zip:
        usds, eurs, gbps, timestamps = [], [], [], []
        for key in keys:
            usds.append(await redis.hget(key, 'usd'))
            eurs.append(await redis.hget(key, 'eur'))
            gbps.append(await redis.hget(key, 'gbp'))
            timestamps.append(await redis.hget(key, 'timestamp'))
        return zip(usds, eurs, gbps, timestamps)

    async def get(self) -> List[dict]:
        redis = await self.connect()
        keys = await self.keys(redis=redis)
        zipped = await self.zipped(redis=redis, keys=keys)
        data = [
            RedisValuesStructure(usd, eur, gbp, timestamp).data()
            for usd, eur, gbp, timestamp in zipped
        ]
        logger.info(RedisLogs.GET_DATA_LOG.format(data=data))
        await self.close()
        return data


class RedisGetUser(RedisConnection):
    async def get(self, key: int | str) -> dict:
        redis = await self.connect()
        username = await redis.hget(key, 'username')
        timestamp = await redis.hget(key, 'timestamp')
        user = RedisUserStructure(
            username=username,
            timestamp=timestamp
        ).data()
        logger.info(RedisLogs.GET_DATA_LOG.format(data=user))
        await self.close()
        return user
