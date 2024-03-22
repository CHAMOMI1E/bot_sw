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


class Marks(Enum):
    ONE: int = 1
    TWO: int = 2
    THREE: int = 3
    FOUR: int = 4
    FIVE: int = 5


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_tg: Mapped[bigint] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), nullable=False)


# class Posts(Base):
#     __tablename__ = "posts"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     photo_before
#     photo_after

