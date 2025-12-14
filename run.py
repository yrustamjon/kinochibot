from aiogram import Bot, Dispatcher
from config import Token
from apps.handlers.main import r as r_main
from apps.handlers.admin import router as r_admin
import asyncio


bot=Bot(token=Token)
dp=Dispatcher()

async def main():
    dp.include_router(r_main)
    dp.include_router(r_admin)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())