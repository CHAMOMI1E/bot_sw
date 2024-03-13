from typing import Annotated

from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from settings.config import TOKEN_DB

bigint = Annotated[int, "BigInteger"]

engine = create_async_engine(TOKEN_DB, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_tg: Mapped[bigint] = mapped_column(BigInteger)



