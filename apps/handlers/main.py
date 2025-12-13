from aiogram import Router
from aiogram.filters import CommandStart
# from apps.keyboards.main_kb import main
from apps.keyboards.admin_kb import choose,admin,movies,movie_bt


r=Router()

@r.message(CommandStart())
async def start(message):
    try: 
       await message.answer(f"salom {message.from_user.first_name+" "+message.from_user.last_name}",
                            reply_markup=movie_bt(1,'back'))
    except :
        await message.answer(
            'salom',
            reply_markup=movie_bt(1,'back')
        )

