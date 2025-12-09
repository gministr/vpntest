import logging

from aiogram.utils.keyboard import InlineKeyboardBuilder

logger = logging.getLogger(__name__)


def keyboard_instructions():
    builder = InlineKeyboardBuilder()
    builder.button(text='Подключиться к впн', callback_data='instructions')
    builder.adjust(2)
    return builder.as_markup()

def keyboard_start():
    builder = InlineKeyboardBuilder()
    builder.button(text='Получить ключ', callback_data='vpn')
    builder.adjust(2)
    return builder.as_markup()


def keyboard_help():
    builder = InlineKeyboardBuilder()
    builder.button(text='Клиенты для подключения', url='https://marzban-docs.sm1ky.com/start/reality_app/')
    return builder.as_markup()


def keyboard_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text='❌Выйти из меню', callback_data='cancel')
    return builder.as_markup()
