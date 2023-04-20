# Aiogram
from aiogram import Dispatcher
from aiogram.types.message import ContentType

# Functions for Handlers
from . import commands
from . import menu


def regCommands(Dp: Dispatcher):
    Dp.register_message_handler(commands.start, state='*', commands='start')


def regMenu(Dp: Dispatcher):
    Dp.register_message_handler(menu.Back_To, state='*', regexp=menu.back_to)
    Dp.register_message_handler(menu.get_menu, state='menu')
    Dp.register_message_handler(menu.get_WeatherMenu, state='weather-menu', content_types=(ContentType.LOCATION, ContentType.TEXT))
    Dp.register_message_handler(menu.get_WeatherCity, state='weather-city')
