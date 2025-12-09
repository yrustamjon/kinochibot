from aiogram import Router
from aiogram.filters import CommandStart

r=Router()

@r.message(CommandStart())
async def start(message):
    await message.answer("salom")