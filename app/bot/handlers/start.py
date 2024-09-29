from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from app.bot.messages import StartMessage
from app.bot.state import UserDataForm

from misc.utils import get_user_data


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext) -> None:
    user_id, username = get_user_data(message=message)
    await state.set_state(UserDataForm.user_id)
    await state.update_data(user_id=user_id)
    await state.set_state(UserDataForm.username)
    await message.answer(StartMessage.MESSAGE.format(username=username))
