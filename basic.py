# MongoDB
from pymongo import MongoClient


# region --Get Weather Icon
def weather_icon(icon):
    icons = {
        '01d': '☀️',      '01n': '🌙',
        '02d': '🌤',         '02n': '☁️',
        '03d': '☁️',      '03n': '☁️',
        '04d': '☁️',      '04n': '☁️',
        '09d': ' 🌦',        '09n': '🌧',
        '10d': '🌧',         '10n': '🌧',
        '11d': '🌩',         '11n': '🌩',
        '13d': '❄️',      '13n': '❄️',
        '50d': '🌫',         '50n': '🌫',
    }
    return icons.get(icon)

# endregion


# region --Loging--
def log(*args):
    if len(args) == 1:
        print(args[0])
    else:
        print(args)


# endregion


# region  --DB--
def get_database():
    Connection_String = "mongodb://localhost:27017/MrCoach"
    Client = MongoClient(Connection_String)
    return Client.get_database()


def get_collection(name: str):
    db = get_database()
    return db.get_collection(name)
# endregion
