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

# Yes / No -- Used in different places
YesNo_Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [Button('Yes'), Button('No')],
        [Button(back_to)]
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

# Menu -> Create Poll -> Poll Option
Finish_Poll = ReplyKeyboardMarkup(
    keyboard=[[Button('Finish')], [Button(back_to)]],
    resize_keyboard=True
)


# Menu -> Create Poll -> Correct option for quiz
def OptionsQuiz_Keyboard(number, data):
    key = InlineKeyboardMarkup()
    for i in range(1, number+1):
        key.row(InButton(text=data.get(f'poll-option-{i}'), callback_data=f'poll-option-{i}'))
    return key
