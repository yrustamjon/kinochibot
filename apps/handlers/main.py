from aiogram import Router
from aiogram.filters import CommandStart,Command
# from apps.keyboards.main_kb import main
from apps.keyboards.admin_kb import choose,admin,movies,movie_bt
from utils.jsonmanager.main import add_json,edit_json
from data.consturucter import user_s


r=Router()

@r.message(CommandStart())
async def start(message):
    try:
        data=user_s(message)
        a=add_json("data/users/list.json",data)
        print(a)
        await message.answer(f"salom {message.from_user.first_name+" "+message.from_user.last_name}",
                            reply_markup=movie_bt(1,'back'))
    except Exception as e:
        print("ERROR:", e)
        await message.answer(
            "salom",
            reply_markup=movie_bt(1, 'back')
        )

