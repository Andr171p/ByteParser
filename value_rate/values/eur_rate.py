from value_rate.source import URL
from value_rate.http_session import HTTPSession

from misc.utils import json_to_dict


class EURRate(HTTPSession):
    @classmethod
    async def eur_to_rub(cls) -> float:
        response = await cls.get_request(url=URL)
        data = json_to_dict(_json=response)
        eur_to_rub = data['Valute']['EUR']['Value']
        return float(eur_to_rub)
