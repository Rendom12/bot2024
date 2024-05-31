# здесь будут хранитьс обработчики @dp

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboars as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет", reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали кнопку помощь!', reply_markup=ReplyKeyboardRemove())


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя", reply_markup=ReplyKeyboardRemove())


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await state.set_state(Register.age)
    await message.answer("Введите ваш возраст")


@router.message (Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age= message.text)
    await state.set_state(Register.number)
    await message.answer("Введите ваш номер телефона", reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nВаше телефон: {data['number']}")
    await state.clear()