import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv("BOT_TOKEN")

# Все обработчики должны быть подключены к Router (или Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с командой `/start`.
    """
    # Большинство объектов события имеют алиасы для API-методов, которые можно вызывать в контексте событий.
    # Например, чтобы ответить на входящее сообщение, можно использовать алиас `message.answer(...)`,
    # и целевой чат будет передан в метод :ref:`aiogram.methods.send_message.SendMessage` автоматически,
    # или вызвать API-метод напрямую через экземпляр Bot: `bot.send_message(chat_id=message.chat.id, ...)`.
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Обработчик отправляет обратно полученное сообщение отправителю.

    По умолчанию обработчик сообщений будет обрабатывать все типы сообщений 
    (например, текст, фото, стикеры и т.д.).
    """
    try:
        # Отправить копию полученного сообщения
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Но не все типы сообщений можно скопировать, поэтому это нужно обрабатывать
        await message.answer("Хорошая попытка!")


async def main() -> None:
    # Инициализация экземпляра Bot с настройками по умолчанию, которые будут применяться ко всем вызовам API
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Запуск обработки событий
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
