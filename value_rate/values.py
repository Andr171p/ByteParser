from value_rate.source import URL
from value_rate.http_session import HTTPSession

from misc.utils import json_to_dict


VALUES = ['USD', 'EUR', 'GBP']


class ValueRate(HTTPSession):
    @classmethod
    async def value_to_rub(cls, value: str = 'USD') -> float:
        response = await cls.get_request(url=URL)
        data = json_to_dict(_json=response)
        gbp_to_rub = data['Valute'][value]['Value']
        return float(gbp_to_rub)
