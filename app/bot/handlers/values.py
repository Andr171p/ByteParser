from aiogram import F, Router
from aiogram.types import Message

from app.bot.keyboards.buttons import ValueRateButtons
from app.bot.keyboards.value_rate_keyboard import value_rate_kb
from app.bot.messages import ValueRateMessage

from storage.settings import RedisSettings
from storage.get import (
    RedisGetValues,
    RedisGetUser
)

from misc.utils import get_user_data


values_router = Router()

redis_get_values = RedisGetValues(url=RedisSettings.VALUES_PUBLIC_URL)
redis_get_user = RedisGetUser(url=RedisSettings.USERS_PUBLIC_URL)


@values_router.message(F.text == ValueRateButtons.USD_RATE_BUTTON)
async def usd_handler(message: Message) -> None:
    user_id, _ = get_user_data(message=message)
    user = await redis_get_user.get(key=user_id)
    username = user['username']
    rates = await redis_get_values.get()
    usd_rate = rates[0]['usd']
    await message.answer(
        ValueRateMessage.USD_MESSAGE.format(
            username=username,
            usd_rate=usd_rate
        ),
        reply_markup=await value_rate_kb()
    )


@values_router.message(F.text == ValueRateButtons.EUR_RATE_BUTTON)
async def eur_handler(message: Message) -> None:
    user_id, _ = get_user_data(message=message)
    user = await redis_get_user.get(key=user_id)
    username = user['username']
    rates = await redis_get_values.get()
    eur_rate = rates[0]['eur']
    await message.answer(
        ValueRateMessage.EUR_MESSAGE.format(
            username=username,
            eur_rate=eur_rate
        ),
        reply_markup=await value_rate_kb()
    )


@values_router.message(F.text == ValueRateButtons.GBP_RATE_BUTTON)
async def eur_handler(message: Message) -> None:
    user_id, _ = get_user_data(message=message)
    user = await redis_get_user.get(key=user_id)
    username = user['username']
    data = await redis_get_values.get()
    gbp_rate = data[0]['gbp']
    await message.answer(
        ValueRateMessage.GBP_MESSAGE.format(
            username=username,
            gbp_rate=gbp_rate
        ),
        reply_markup=await value_rate_kb()
    )
