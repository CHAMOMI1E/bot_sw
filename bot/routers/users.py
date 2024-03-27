from aiogram import Router, types
from aiogram.filters import CommandStart

from db.requests.user_requests import get_user_by_id_tg

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message):
    user = await get_user_by_id_tg(message.from_user.id)
    if user:
        await message.answer("Вы находитесь в главном меню")
    else:
        await message.answer(
            f"Здравствуйте {message.from_user.first_name}! \n"
            f"Этот бот создан для вашей связь с нами, а так же посмотреть работы.\n"
            f"Вы сейчас находитесь в главном меню")
