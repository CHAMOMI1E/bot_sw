from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.keyboards.main_menu import main_menu_kb, request_a_call_kb
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
            f"Здравствуйте {message.from_user.first_name}! \n"
            f"Этот бот создан для вашей связь с нами, а так же посмотреть работы.\n"
            f"Вы сейчас находитесь в главном меню", reply_markup=main_menu_kb())


@user_router.callback_query(F.data == "request-a-call")
async def requests_a_call(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Отправьте свой номер телефона", reply_markup=request_a_call_kb())
    await state.set_state(PhoneRequest.phone)


@user_router.message(PhoneRequest.phone)
async def request_text(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()
    await state.clear()
    await message.answer(message.contact)
