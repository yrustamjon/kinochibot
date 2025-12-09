from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎬 Kinolar",callback_data="movies"),
            InlineKeyboardButton(text="🔍 Qidiruv",callback_data="search")
        ],
        [
            InlineKeyboardButton(text="⭐ Top kinolar",callback_data="top_list"),
            InlineKeyboardButton(text="🧾 Profil",callback_data="profile")
        ],
        [
            InlineKeyboardButton(text="💎 Premium Subscribe",callback_data="subscribe")
        ]
    ]
)

# 🎬 Kinolar
# 🔍 Qidiruv
# ⭐ Top kinolar
# 🧾 Profil