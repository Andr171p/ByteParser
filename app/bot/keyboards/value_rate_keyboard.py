from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

from app.bot.keyboards.buttons import ValueRateButtons


async def value_rate_kb() -> ReplyKeyboardMarkup:
    kb_list = [
        [KeyboardButton(text=ValueRateButtons.USD_RATE_BUTTON)],
        [KeyboardButton(text=ValueRateButtons.EUR_RATE_BUTTON)],
        [KeyboardButton(text=ValueRateButtons.GBP_RATE_BUTTON)]
    ]
    kb = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Узнать курс валюты"
    )
    return kb
