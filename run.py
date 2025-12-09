from aiogram import Bot, Dispatcher
from config import Token
from apps.handlers.main import r as r_main
import asyncio


bot=Bot(token=Token)
dp=Dispatcher()

async def main():
    dp.include_router(r_main)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())