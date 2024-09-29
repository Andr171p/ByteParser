from value_rate.values import (
    usd_rate,
    eur_rate,
    gbp_rate
)

from storage.set import redis_set

from misc.utils import (
    today,
    timestamp
)


async def task() -> None:
    usd = await usd_rate.USDRate.usd_to_rub()
    eur = await eur_rate.EURRate.eur_to_rub()
    gbp = await gbp_rate.GBPRate.usd_to_rub()
    await redis_set.set(
        key=today(),
        usd=usd,
        eur=eur,
        gbp=gbp,
        timestamp=timestamp()
    )
