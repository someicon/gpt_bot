from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

user_private_router = Router()

@user_private_router.message(Command('start_gpt'))
async def start_gpt(message: Message):
    await message.answer("123")
