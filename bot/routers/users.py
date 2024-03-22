from aiogram import Router, types
from aiogram.filters import CommandStart

from db.requests.user_requests import get_user_by_id_tg

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message):
    user = await get_user_by_id_tg(message.from_user.id)
    if user:
        pass
    else:
        pass
