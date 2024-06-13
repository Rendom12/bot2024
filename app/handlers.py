# здесь будут хранитьс обработчики @dp

from aiogram import F, Router, html
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboars as kb
import database.requests as rq

router = Router()


class Form(StatesGroup):
    sell_buy = State()
    selling_name = State()
    name = State()
    phone = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}! Давайте начнем заполнять анкету.", reply_markup= kb.start_keyboards)
    # await message.answer("Привет", reply_markup=kb.main)
    await rq.set_user(message.from_user.id, message.from_user.first_name)


# Обработчик кнопки "Кнопка 1"
@router.message(lambda message: message.text == kb.available[0])
async def button1_handler(message: Message, state: FSMContext):
    await state.set_state(Form.sell_buy)
    await state.update_data(sell_buy= 1)   # 1 - это ПРОДАЖА клиента
    await state.set_state(Form.selling_name)
    await message.answer("Что продаете? ", reply_markup=ReplyKeyboardRemove())

@router.message(Form.selling_name)
async def process_selling_name(message: Message, state: FSMContext):
    await state.update_data(selling_name=message.text)
    await message.answer(
        f"Какой год производства  {html.quote(str(message.text))}?")
    await state.set_state(Form.name)
    # await message.answer("Как Вас зовут?? ", reply_markup=ReplyKeyboardRemove())



@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer("Введите ваш номер телефона", reply_markup=kb.get_number)


@router.message(Form.phone, F.contact)
async def process_number(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()
    # await message.answer(f"Вы продаете\покупаете: {data['sell_buy']}\nЧто продаете: {data['selling_name']}\nВаше имя: {data['name']}\nВаше телефон: {data['phone']}", reply_markup=ReplyKeyboardRemove())

    # await rq.set_user(message.from_user.id, message.from_user.first_name, phone = data['number'], sell_buy= data['sell_buy'], salling_name = data['selling_name'])
    await rq.f_user(data, message.from_user.id)

    await state.clear()






@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали кнопку помощь!', reply_markup=ReplyKeyboardRemove())