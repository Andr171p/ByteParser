from redis import Redis

from storage.connection import RedisConnection
from storage.structure import RedisStructure
from storage.logs import RedisLogs

from loguru import logger

from typing import List


class RedisGet(RedisConnection):
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

    @classmethod
    async def get(cls) -> List[dict]:
        redis = await cls.connect()
        keys = await cls.keys(redis=redis)
        zipped = await cls.zipped(redis=redis, keys=keys)
        data = [
            RedisStructure(usd, eur, gbp, timestamp).data()
            for usd, eur, gbp, timestamp in zipped
        ]
        logger.info(RedisLogs.GET_DATA_LOG.format(data=data))
        await cls.close()
        return data


redis_get = RedisGet()
