# Aiogram
from aiogram import Dispatcher
from aiogram.types.message import ContentType

# Functions for Handlers
from . import commands
from . import menu
from . import poll
from keyboards.general import back_to


def regCommands(Dp: Dispatcher):
    Dp.register_message_handler(commands.start, state='*', commands='start')


def regMenu(Dp: Dispatcher):
    Dp.register_message_handler(menu.Back_To, state='*', regexp=back_to)
    Dp.register_message_handler(menu.get_menu, state='menu')
    Dp.register_message_handler(menu.get_WeatherMenu, state='weather-menu', content_types=(ContentType.LOCATION, ContentType.TEXT))
    Dp.register_message_handler(menu.get_WeatherCity, state='weather-city')
    Dp.register_message_handler(menu.get_Currency, state='currency')


def regPoll(Dp: Dispatcher):
    Dp.register_message_handler(poll.get_pollTitle, state='poll-title')
    Dp.register_message_handler(poll.get_pollAnonymous, state='poll-anonymous')
    Dp.register_message_handler(poll.get_pollQuiz, state='poll-quiz')
    Dp.register_message_handler(poll.get_pollOption, state='poll-option')
    Dp.register_message_handler(poll.get_pollMultiAns, state='poll-multi-ans')
    Dp.register_callback_query_handler(poll.get_pollQuizAns, state='poll-quiz-ans')
