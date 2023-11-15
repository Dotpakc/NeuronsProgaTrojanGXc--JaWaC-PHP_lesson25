# Створіть Telegram-бота, 
# який може відповідати на дві команди: 
#     /hello та /time. Команда /hello має 
#     призвести до вітання користувача з власним іменем. 
#     Команда /time повинна виводити поточний час. 
#     Крім того, бот повинен вміти реагувати на будь-які інші 
#     повідомлення користувача, надсилаючи відповідь у формі 
#     'Я не розумію вас. Доступні команди: /hello, /time'. 
#     Вам слід використовувати бібліотеку Aiogram для 
#     реалізації бота та виводу повідомлень."

# Скинути лінк репозіторія на бота в github. 
# як показував на уроці. Повинно бути як показував на уроці. 
# всі файли та нічого зайвого


from aiogram import Bot, Dispatcher
from decouple import config

API_TOKEN = config("TELEGRAM_API_TOKEN")

# bot = Bot(token=API_TOKEN)
import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from time import time
from datetime import time, date

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    print(message)
    print(message.chat)
    await message.answer("бот запустився")


@dp.message(Command("Hello"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("time"))
async def command_start_handler(message: types.Message):
    await message.answer(f"current time :{message.date}")
    text = f"current time{message.date.strftime('%H:%M:%S')}"


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send a copy of the received message
        await message.answer("я не розумію вас")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())