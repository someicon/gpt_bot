from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from g4f.client import Client

from keyboards.reply import get_keyboard

user_private_router = Router()


START_KB = get_keyboard(
    "Задать вопрос",
    "Выйти",
    placeholder="Выберете действие",
    sizes=(2, )
)


@user_private_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в чат!", reply_markup=START_KB)

# FSM

class AskQuestion(StatesGroup):
    question = State()

@user_private_router.message(F.text == "Задать вопрос")
async def start_gpt(message: Message, state: FSMContext):
    await state.set_state(AskQuestion.question)
    await message.answer("Введите запрос", reply_markup=ReplyKeyboardRemove())


@user_private_router.message(AskQuestion.question)
async def ask_gpt(message: Message, state: FSMContext):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{message.text}"}],
    )
    gpt_answer = response.choices[0].message.content

    await message.answer(f"{gpt_answer}", reply_markup=START_KB)
    await state.clear()
