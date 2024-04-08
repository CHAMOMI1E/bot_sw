from enum import Enum
from typing import Annotated
from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from settings.config import TOKEN_DB

bigint = Annotated[int, "BigInteger"]

engine = create_async_engine(TOKEN_DB, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Roles(Enum):
    USER: str = 'USER'
    ADMIN: str = 'ADMIN'
    DEVELOPER: str = 'DEVELOPER'


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_tg: Mapped[bigint] = mapped_column(BigInteger)
    role: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), nullable=False)



