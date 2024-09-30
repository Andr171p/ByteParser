from value_rate.values import ValueRate

from storage.set import RedisSetValues
from storage.manager import RedisManager
from storage.settings import RedisSettings

from misc.utils import today


redis_url = RedisSettings.VALUES_PUBLIC_URL

redis_set = RedisSetValues(url=redis_url)
redis_manager = RedisManager(url=redis_url)


async def get_values() -> tuple[float, float, float]:
    usd = await ValueRate.value_to_rub(value='USD')
    eur = await ValueRate.value_to_rub(value='EUR')
    gbp = await ValueRate.value_to_rub(value='GBP')
    return usd, eur, gbp


async def task() -> None:
    await redis_manager.clear()
    usd, eur, gbp = await get_values()
    await redis_set.set(
        key=today(),
        usd=usd,
        eur=eur,
        gbp=gbp
    )
