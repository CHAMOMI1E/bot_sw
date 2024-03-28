from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.decorators.dec_for_kb import kb_wrap


@kb_wrap(keyboard_type='inline', adjust_keyboard=(1,))
def main_menu_kb(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text='Заказать звонок', callback_data='request-a-call')


@kb_wrap(keyboard_type='reply', adjust_keyboard=(1,))
def request_a_call_kb(builder: ReplyKeyboardBuilder) -> ReplyKeyboardMarkup:
    builder.button(text='Поделится своим контаком', request_contact=True)
