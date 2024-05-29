import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import  Message

bot = Bot(token= '5881506855:AAGzrrsifHuhx8HGgQbon10YCdyxjlpef0A')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())