from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.keyboards.main_menu import main_menu_kb, request_a_call_kb, back_to_menu_kb
from bot.utils.states import PhoneRequest
from db.requests.user_requests import get_user

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    user = await get_user(message.from_user.id)
    if user:
        await message.answer("Вы находитесь в главном меню бота", reply_markup=main_menu_kb())
    else:
        await message.answer(
            f"Здравствуйте {message.from_user.first_name}, {message.reply_to_message}! \n"
            f"Этот бот создан для вашей связь с нами, а так же посмотреть работы.\n"
            f"Вы сейчас находитесь в главном меню", reply_markup=main_menu_kb())


@user_router.callback_query(F.data == "request-a-call")
async def requests_a_call(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
        "Введите свой номер телефона (+375XXXXXXXXX / 375XXXXXXXXX)\n"
        "или нажмите на кнопку 'поделится контактом'",
        reply_markup=request_a_call_kb())
    await state.set_state(PhoneRequest.phone)


@user_router.message(PhoneRequest.phone)
async def request_text(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(phone=message.text)
    else:
        await state.update_data(phone=message.contact.phone_number.replace('+', ''))
    data = await state.get_data()
    if data['phone'].isdigit():
        await message.answer(data['phone'], reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Вы ввели неправильно номер телефона", reply_markup=request_a_call_kb())
        await state.set_state(PhoneRequest.phone)


@user_router.callback_query(F.data == "back-to-menu")
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("Вы сейчас находитесь в главном меню", reply_markup=main_menu_kb())
