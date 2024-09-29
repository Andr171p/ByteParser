from value_rate.source import URL
from value_rate.http_session import HTTPSession

from misc.utils import json_to_dict


class GBPRate(HTTPSession):
    @classmethod
    async def usd_to_rub(cls) -> float:
        response = await cls.get_request(url=URL)
        data = json_to_dict(_json=response)
        gbp_to_rub = data['Valute']['GBP']['Value']
        return float(gbp_to_rub)