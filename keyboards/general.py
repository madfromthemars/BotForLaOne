# Aiogram
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton)

Remove = ReplyKeyboardRemove()
Button = KeyboardButton
InButton = InlineKeyboardButton
back_to = 'Back ⬅️'


# Back -- Used in different places
Back_Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [Button(text=back_to)]
    ], resize_keyboard=True
)


# Menu
Menu_Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [Button(text='Current Weather')],
        [Button(text='Convert currency')],
        [Button(text='Create a Poll')],
        [Button(text='Cheer Me UP')],
    ], resize_keyboard=True
)

# Menu -> Current Weather (Options)
WeatherMenu_Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [Button(text='By City')],
        [Button(text='By Current Location', request_location=True)],
        [Button(text=back_to)]
    ], resize_keyboard=True
)


