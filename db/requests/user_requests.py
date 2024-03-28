from sqlalchemy import select

from db.models import Users, async_session


async def get_user(id_tg: int) -> Users:
    try:
        async with async_session() as session:
            result = await session.execute(select(Users).filter_by(id_tg=id_tg))
            return result.scalars().first()
    except Exception as e:
        print(e)
        return None
