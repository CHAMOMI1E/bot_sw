from typing import Optional, Union, Tuple

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

from settings.config import TOKEN_BOT


async def send_message(text: str, chat_id: int, kb: Optional[
    Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]
] = None) -> None:
    bot_sender = Bot(TOKEN_BOT)
    try:
        await bot_sender.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=kb,
        )
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        await bot_sender.session.close()


async def send_spam(
        text: str,
        chat_ids: Tuple[int],
        kb: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove]] = None
) -> None:
    bot_sender = Bot(TOKEN_BOT)
    try:
        for chat_id in chat_ids:
            await bot_sender.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=kb,
            )
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        await bot_sender.session.close()
