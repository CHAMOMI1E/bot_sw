from aiogram.filters import BaseFilter
from aiogram import types
from db.requests.filters_requests import search_admin


class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        account = await search_admin(message.from_user.id)
        if account:
            return True
        else:
            return False

