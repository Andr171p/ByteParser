from sqlalchemy import select

from database.db import DataBaseSessionManager
from database.models.users_model import UserModel

from typing import Sequence


class ORMManager(DataBaseSessionManager):
    def __init__(self) -> None:
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UserModel.metadata.drop_all)
            await connection.run_sync(UserModel.metadata.create_all)

    async def create_user(self, user_id: int, username: str) -> UserModel:
        async with self.session() as session:
            user = UserModel(
                user_id=user_id,
                username=username
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> None:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            user = user.scalar()
            try:
                await session.delete(user)
                await session.commit()
            except:
                raise Exception("User not found")

    async def get_user(self, user_id: int) -> UserModel:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.user_id == user_id)
            )
            if user:
                return user.scalars().one()
            else:
                raise Exception("User not found")

    async def get_username(self, user_id: int) -> str:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel.username).where(UserModel.user_id == user_id)
            )
            if user:
                return user.scalars().one()
            else:
                raise Exception("User not found")

    async def get_users(self) -> Sequence[UserModel]:
        async with self.session() as session:
            users = await session.execute(
                select(UserModel)
            )
            return users.scalars().all()

    async def clear_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UserModel.metadata.drop_all)
            await connection.run_sync(UserModel.metadata.create_all)


orm_manager = ORMManager()
