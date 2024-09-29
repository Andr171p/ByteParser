from aiogram import F, Router
from aiogram.types import Message

from app.bot.keyboards.buttons import ValueRateButtons
from app.bot.keyboards.value_rate_keyboard import value_rate_kb
from app.bot.messages import ValueRateMessage

from database.orm_manager import orm_manager

from storage.get import redis_get

from misc.utils import get_user_data

values_router = Router()


@values_router.message(F.text == ValueRateButtons.USD_RATE_BUTTON)
async def usd_handler(message: Message) -> None:
    user_id, _ = get_user_data(message=message)
    username = await orm_manager.get_username(user_id=user_id)
    data = await redis_get.get()
    usd_rate = data[0]['usd']
    await message.answer(
        ValueRateMessage.MESSAGE.format(
            username=username,
            usd_rate=usd_rate
        ),
        reply_markup=await value_rate_kb()
    )
