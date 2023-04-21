# Built In
import os
import random

# .env
from dotenv import load_dotenv

IMAGE_DIR = 'images/'

# region --Get Weather Icon
def weather_icon(icon):
    icons = {
        '01d': '☀️', '01n': '🌙',
        '02d': '🌤', '02n': '☁️',
        '03d': '☁️', '03n': '☁️',
        '04d': '☁️', '04n': '☁️',
        '09d': ' 🌦', '09n': '🌧',
        '10d': '🌧', '10n': '🌧',
        '11d': '🌩', '11n': '🌩',
        '13d': '❄️', '13n': '❄️',
        '50d': '🌫', '50n': '🌫',
    }
    return icons.get(icon)


# endregion

# region --Config from ENV--
load_dotenv()
TOKEN: str = os.getenv('TOKEN')
DB_HOST: str = os.getenv('DB_HOST')
DB_PORT: str = os.getenv('DB_PORT')
DB_NAME: str = os.getenv('DB_NAME')
OWM_TOKEN: str = os.getenv('OWM_TOKEN')
CF_TOKEN: str = os.getenv('CF_TOKEN')


# endregion

# region --Loging--
def log(*args):
    if len(args) == 1:
        print(args[0])
    else:
        print(args)


# endregion

# region --Random Image--
def get_RandomImage():
    images = os.listdir(IMAGE_DIR)
    imageName = random.choice(images)
    Image = open(IMAGE_DIR + imageName, 'rb')
    return Image

# endregion
