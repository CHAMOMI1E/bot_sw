from db.models import async_session, Roles, Users
from sqlalchemy import select


async def search_admin(id_tg) -> Users or None:
    async with async_session() as session:
        try:
            blocks = await session.execute(
                select(Users)
                .where(Users.role.in_([Roles.ADMIN.value, Roles.DEVELOPER.value]))
                .where(Users.id_tg == id_tg)
            )
            return blocks.scalars().first()
        except Exception as e:
            print(e)
            return None
