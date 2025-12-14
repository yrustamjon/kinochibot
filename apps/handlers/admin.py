from aiogram import Router,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import  Command
from apps.keyboards.admin_kb import( choose as choose_kb)
from apps.keyboards.admin_kb import(admin as admin_kb)
from apps.keyboards.main_kb import(main as main_kb)
from apps.keyboards.admin_kb import(movies as movies_kb)
from apps.keyboards.admin_kb import(users as users_kb)

router = Router()


@router.message(Command("choose"))
async def choose(message):
    await message.answer("Hello admin", reply_markup=choose_kb)

# admin,user
@router.callback_query(F.data=="admin")
async def admin(call):
    await call.message.edit_text("Admin panel", reply_markup=admin_kb)

@router.callback_query(F.data=="user")
async def user(call):
    await call.message.edit_text("User panel", reply_markup=main_kb)

# movies, users, ads

@router.callback_query(F.data=="movies")
async def movies(call):
    await call.message.edit_text("Movies panel", reply_markup=movies_kb)
    

@router.callback_query(F.data=="users")
async def users(call):
    await call.message.edit_text("Users panel", reply_markup=users_kb)

@router.callback_query(F.data=="ads")
async def ads(call):
    await call.message.edit_text(
        "Ads panel", 
        reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Back",callback_data="admin")
            ]
        ]
    ))


#admins, top_users, premium_users,x
