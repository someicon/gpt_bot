from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

user_private_router = Router()

@user_private_router.message(Command('gpt'))
