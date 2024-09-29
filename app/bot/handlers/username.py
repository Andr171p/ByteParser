from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.logs import bot_logs
from app.bot.state import UserDataForm
from app.bot.messages import UserNameMessage
from app.bot.keyboards.value_rate_keyboard import value_rate_kb

from database.orm_manager import orm_manager

from loguru import logger


username_router = Router()


@username_router.message(UserDataForm.username)
async def username_handler(message: Message, state: FSMContext) -> None:
    username = message.text
    await state.update_data(username=username)
    user_data = await state.get_data()
    user_id, username = user_data['user_id'], user_data['username']
    _user = await orm_manager.create_user(
        user_id=user_id,
        username=username
    )
    logger.info(bot_logs.CREATE_USER_LOG.format(user=_user))
    await message.answer(
        UserNameMessage.MESSAGE.format(username=username),
        reply_markup=await value_rate_kb()
    )
    await state.clear()
