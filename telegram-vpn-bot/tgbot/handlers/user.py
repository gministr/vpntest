from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import bot
from tgbot.keyboards.inline import keyboard_start, keyboard_help, keyboard_instructions

user_router = Router()


@user_router.message(Command('start'))
async def user_start(message: Message):
    await message.answer('Приветственное сообщение, тест выдачи индивидуального ключа',
                         reply_markup=keyboard_instructions(), disable_web_page_preview=True)


@user_router.callback_query(F.data == 'instructions')
async def vpn_instruct(callback: CallbackQuery):
    await callback.message.answer('🤓 Как подключиться:\n1️⃣ Скачайте подходящее для вашего устройства приложение \n\n2️⃣ Добавьте ваш персональный ключ в приложение\n\n3️⃣ Подключитесь к VPN в приложении', 
                                  reply_markup=keyboard_start)