from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.logs import bot_logs
from app.bot.state import UserDataForm
from app.bot.messages import UserNameMessage
from app.bot.keyboards.value_rate_keyboard import value_rate_kb

from database.orm_manager import orm_manager

from storage.set import RedisSetUser
from storage.manager import RedisManager
from storage.settings import RedisSettings

from loguru import logger


username_router = Router()

redis_url = RedisSettings.USERS_PUBLIC_URL

redis_set_user = RedisSetUser(url=redis_url)
redis_manager = RedisManager(url=redis_url)


@username_router.message(UserDataForm.username)
async def username_handler(message: Message, state: FSMContext) -> None:
    await message.answer(UserNameMessage.REGISTER_MESSAGE)
    username = message.text
    await state.update_data(username=username)
    user_data = await state.get_data()
    user_id, username = user_data['user_id'], user_data['username']
    await orm_manager.delete_user(user_id=user_id)
    _user = await orm_manager.create_user(
        user_id=user_id,
        username=username
    )
    await redis_manager.delete(key=user_id)
    await redis_set_user.set(
        key=user_id,
        username=username
    )
    logger.info(bot_logs.CREATE_USER_LOG.format(user=_user))
    # await message.delete()
    await message.answer(
        UserNameMessage.MESSAGE.format(username=username),
        reply_markup=await value_rate_kb()
    )
    await state.clear()
