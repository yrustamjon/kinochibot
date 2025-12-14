from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👑 Admin Panel", callback_data="admin")
        ],
        [
            InlineKeyboardButton(text="🎥 User Mode", callback_data="user")
        ]
    ]
)


admin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎬 Movies",callback_data="movies"),
            InlineKeyboardButton(text='👥 Users',callback_data="users")
        ],
        [
            InlineKeyboardButton(text="📢 Ads",callback_data='ads')
        ]
    ]
)

movies=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕ Add Movie',callback_data="add_movie")
        ],
        [
            InlineKeyboardButton(text='📁 All Movies',callback_data='list_movie'),
            InlineKeyboardButton(text='🔍 Search',callback_data="search")
        ],
        [
            InlineKeyboardButton(text='⬅️ Back',callback_data='admin')
        ]
    ]
)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class MovieAction(CallbackData, prefix="movie"):
    action: str
    movie_id: int


def movie_bt(movie_id: int, back: str):
    kb = InlineKeyboardBuilder()

    kb.button(
        text="📝 Edit Movie",
        callback_data=MovieAction(action="edit", movie_id=movie_id).pack()
    )
    
    kb.button(
        text="❌ Delete Movie",
        callback_data=MovieAction(action="delete", movie_id=movie_id).pack()
    )

    kb.button(
        text="📊 Movie Stats",
        callback_data=MovieAction(action="stats", movie_id=movie_id).pack()
    )

    kb.button(
        text="⬅️ Back",
        callback_data=back
    )
    kb.adjust(1)
    return kb.as_markup()


users = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👮 Admin', callback_data='admins')
        ],
        [
            InlineKeyboardButton(text='🏆 Top Users', callback_data='top_users'),
            InlineKeyboardButton(text='💎 Premium Users', callback_data='premium_users')
        ],
        [
            InlineKeyboardButton(text='X', callback_data='x')
        ],
        [
            InlineKeyboardButton(text='🔙 Back', callback_data='admin')
        ]
    ]
)
