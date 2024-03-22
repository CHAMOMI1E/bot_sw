from sqlalchemy import select

from db.models import Users, async_session


async def get_user_by_id_tg(id_teleg: int) -> Users:
    async with async_session() as session:
        result = await session.execute(select(Users).filter_by(id_tg=id_teleg))
        existing_user = result.scalars().first()
        return existing_user

