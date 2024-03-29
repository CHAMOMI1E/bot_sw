from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.decorators.dec_for_kb import kb_wrap


@kb_wrap(keyboard_type='inline', adjust_keyboard=(1,))
def main_menu_kb(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    ReplyKeyboardRemove()
    builder.button(text='Заказать звонок', callback_data='request-a-call')


@kb_wrap(keyboard_type='reply', adjust_keyboard=(1,), one_time_keyboard=True)
def request_a_call_kb(builder: ReplyKeyboardBuilder) -> ReplyKeyboardMarkup:
    builder.button(text='Поделится своим контаком', request_contact=True)


@kb_wrap(keyboard_type="inline", adjust_keyboard=1)
def back_to_menu_kb(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text="← Вернуться в главное меню", callback_data="back-to-menu")


