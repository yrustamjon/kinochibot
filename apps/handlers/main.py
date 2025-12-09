from aiogram import Router
from aiogram.filters import CommandStart
from apps.keyboards.main_kb import main


r=Router()

@r.message(CommandStart())
async def start(message):
    await message.answer("salom",reply_markup=main)