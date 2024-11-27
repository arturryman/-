from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram import Router
import os
import asyncio

# Загрузка токена 
TOKEN = '8149796529:AAFLmeDPUKxYLsRLxO_gB3pdwG6TFL1l2l4'

# Создание бота
bot = Bot(token=TOKEN)

# Создание диспетчера
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот, который пересылает сообщения в группу.")

@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Используйте /start для начала работы.")

@router.message(F.text)
async def forward_message(message: types.Message):
    chat_id = 344890333  # идентификатор группы

    # Проверяем, является ли сообщение из группы
    if message.chat.type in ['group', 'supergroup']:
        return  # Если сообщение из группы, ничего не делаем

    # Если сообщение не из группы, пересылаем его в группу
    await bot.forward_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Сообщение переслано в группу.")

# Регистрация маршрутизатора
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
