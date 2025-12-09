from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Admin", callback_data="admin"),
            InlineKeyboardButton(text="User",callback_data="user")
        ]
    ]
)

admin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Movies",callback_data="movies"),
            InlineKeyboardButton(text='Users',callback_data="users")
        ],
        [
            InlineKeyboardButton(text="Ad",callback_data='ad')
        ]
    ]
)