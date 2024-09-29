from aiogram.filters.state import (
    State,
    StatesGroup
)


class UserDataForm(StatesGroup):
    user_id = State()
    username = State()
