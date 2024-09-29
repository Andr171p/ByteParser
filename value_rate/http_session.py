import aiohttp
from aiohttp import ClientResponse

from loguru import logger

from value_rate.logs import http_logs

from misc.utils import bytes_to_json


class HTTPSession:
    @staticmethod
    def is_ok(response: ClientResponse) -> bool:
        status_code = response.status
        logger.info(http_logs.RESPONSE_RECEIVED.format(status_code=status_code))
        return True if status_code in range(200, 300) else False

    @classmethod
    async def get_request(cls, url: str, timeout: int = 5) -> str | None:
        try:
            async with aiohttp.ClientSession() as session:
                logger.info(http_logs.START_REQUEST_LOG.format(url=url))
                async with session.get(
                        url=url,
                        headers={'Content-Type': 'application/json'},
                        timeout=timeout
                ) as response:
                    if cls.is_ok(response=response):
                        _bytes = await response.read()
                        _json = bytes_to_json(_bytes=_bytes)
                        # logger.info(http_logs.RESPONSE_DATA.format(_json=_json))
                        return _json
        except Exception as _ex:
            logger.warning(_ex)