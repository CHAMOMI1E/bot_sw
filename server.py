import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from settings.config import TOKEN_BOT
from bot.routers.users_router import user_router

bot = Bot(TOKEN_BOT, parse_mode=ParseMode.HTML)
dp = Dispatcher()


async def start_bot() -> None:
    dp.include_routers(user_router,)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
                        stream=sys.stdout)
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Shutting down')
