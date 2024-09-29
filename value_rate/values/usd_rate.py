from value_rate.source import URL
from value_rate.http_session import HTTPSession
from value_rate.logs import HTTPLogs

from misc.utils import json_to_dict

from loguru import logger


class USDRate(HTTPSession):
    @classmethod
    async def usd_to_rub(cls) -> float:
        response = await cls.get_request(url=URL)
        data = json_to_dict(_json=response)
        usd_to_rub = data['Valute']['USD']['Value']
        logger.info(HTTPLogs.USD_RATE_LOG.format(usd_rate=usd_to_rub))
        return float(usd_to_rub)
