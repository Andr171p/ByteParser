from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

import contextlib
from typing import AsyncIterator, Optional

from database.settings import PostgreSQLSettings


class DataBaseSessionManager:
    _engine: Optional[AsyncEngine] = None
    _sessionmaker: Optional[async_sessionmaker[AsyncSession]] = None

    @classmethod
    def init(cls) -> None:
        cls._engine = create_async_engine(
            PostgreSQLSettings.PUBLIC_URL,
            echo=True
        )
        cls._sessionmaker = async_sessionmaker(
            bind=cls._engine,
            expire_on_commit=False
        )

    @classmethod
    async def close(cls) -> None:
        if cls._engine is None:
            return
        await cls._engine.dispose()
        cls._engine = None
        cls._sessionmaker = None

    @classmethod
    @contextlib.asynccontextmanager
    async def session(cls) -> AsyncSession:
        async with cls._sessionmaker() as session:
            try:
                yield session
            except Exception as _ex:
                await session.rollback()
                raise _ex

    @classmethod
    @contextlib.asynccontextmanager
    async def connect(cls) -> AsyncIterator[AsyncConnection]:
        if cls._engine is None:
            raise IOError("DatabaseSessionManager is not initialized")
        async with cls._engine.begin() as connection:
            try:
                yield connection
            except Exception as _ex:
                await connection.rollback()
                raise _ex


db_manager = DataBaseSessionManager()


async def get_session() -> AsyncSession:
    async with db_manager.session() as session:
        yield session
