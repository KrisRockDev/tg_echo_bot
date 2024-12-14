
# Это эхо-бот.
# Он повторяет любые входящие текстовые сообщения.

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.webhook import executor  # Исправленный импорт

API_TOKEN = 'BOT TOKEN HERE'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Этот хэндлер вызывается, когда пользователь отправляет команды `/start` или `/help`.
    """
    await message.reply("Привет!\nЯ ЭхоБот!\nРаботаю на aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    """
    Этот хэндлер отправляет изображение котов, если сообщение содержит "cat" или "puss".
    """
    try:
        with open('data/cats.jpg', 'rb') as photo:
            await bot.send_photo(
                message.chat.id, photo, caption='Коты здесь 😺',
                reply_to_message_id=message.message_id
            )
    except FileNotFoundError:
        await message.reply("Файл с изображением котов не найден.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    Этот хэндлер повторяет любое текстовое сообщение пользователя.
    """
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)