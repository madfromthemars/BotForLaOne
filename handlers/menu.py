# Aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext

# Keyboard
from keyboards.general import WeatherMenu_Keyboard, Menu_Keyboard, Back_Keyboard

# Local
from basic import log, weather_icon
from owm import owmByLocation, owmByCity
from cf import get_currency

menu_option_text = [
    'Please choose from options below😀', 'Pleas choose from options below☺️',
    'Options are liston on your device as buttons🙂',
    'If you there is not button just send /start', 'Buttons are listed below!👇👇👇', 'Buttons buddy😤',
    'BUTTONS😠', 'ok! I got you!😌', 'OK! I GOT YOU!!! 😑', 'WHAT YOU NEED FROM ME!!! 😡',
    " *&%$ 🤬"
]


async def Back_To(message: types.Message, state: FSMContext):
    Current_State = await state.get_state()
    if Current_State in ('weather-menu', 'currency'):
        await message.answer(message.text, reply_markup=Menu_Keyboard)
        await state.set_state('menu')
    elif Current_State in 'weather-city':
        await message.answer(message.text, reply_markup=WeatherMenu_Keyboard)
        await state.set_state('weather-menu')
    log(message.from_user.username, Current_State, message.text)


# Responses In -> Menu State
async def get_menu(message: types.Message, state: FSMContext):
    log(message.from_id, '__Menu__', message.text)

    if message.text == 'Current Weather':
        await message.answer(message.text, reply_markup=WeatherMenu_Keyboard)
        await state.set_state('weather-menu')
    elif message.text == 'Convert currency':
        await message.answer(
            "Send in this format:\nAmount - from Current - to Currency"
            "\n\nExample: 100-eur-rub"
            "\n\n<i>Please note that use Abbreviations for currency</i>",
            reply_markup=Back_Keyboard,
            parse_mode="HTML"
        )
        await state.set_state('currency')
    elif message.text == 'Create a Poll':
        await message.answer(message.text)
    elif message.text == 'Cheer Me UP':
        await message.answer(message.text)
    else:
        data = await state.get_data()
        menu_attempt = data.get('menu_attempt') or 0
        if menu_attempt == 1:
            await message.answer('Hmm...')
            await message.answer(
                "You should know that I'm Bot. \nI have limited option what can I do. \nSo I don't know what you need."
            )
        menu_attempt += 1
        if menu_attempt < len(menu_option_text):
            await message.answer(menu_option_text[menu_attempt])
        await state.update_data(menu_attempt=menu_attempt)


# Responses In -> Weather-Menu State
async def get_WeatherMenu(message: types.Message, state: FSMContext):
    log(message.from_id, '__Weather-Menu__', message.text or message.location)

    if message.location:
        res = owmByLocation(message.location.latitude, message.location.longitude, message.from_user.language_code)
        if res:
            wi = weather_icon(res['weather'][0]['icon'])
            txt = f"{res['name']}, {res['sys']['country']}" \
                  f"\n{res['weather'][0]['main']} {res['weather'][0]['description']} {wi}" \
                  f"\nTemperature: {int(res['main']['temp'])}°K | {int(res['main']['temp'] - 273.15)}°C" \
                  f"\nWind 🌬 -- {res['wind']['speed']}m/s" \
                  f"\nPercentage of cloudiness -- {res['clouds']['all']}%"
            await message.answer(txt)
        else:
            await message.answer("Something went wrong. Please try later or connect ot @...")
    elif message.text == 'By City':
        await message.answer("Please send your city name", reply_markup=Back_Keyboard)
        await state.set_state("weather-city")
    else:
        return


# Responses In -> Weather-Menu -> Weather-City State
async def get_WeatherCity(message: types.Message, state: FSMContext):
    log(message.from_id, '__Weather-Menu__', message.text or message.location)
    if '&' in message.text or '=' in message.text or ',' in message.text:
        await message.answer('Incorrect Format')
        return

    res = owmByCity(message.text, message.from_user.language_code)
    if res.get('message') == 'city not found':
        await message.answer('City not found')
        return
    else:
        try:
            wi = weather_icon(res['weather'][0]['icon'])
            txt = f"{res['name']}, {res['sys']['country']}" \
                  f"\n{res['weather'][0]['main']} {res['weather'][0]['description']} {wi}" \
                  f"\nTemperature: {int(res['main']['temp'])}°K | {int(res['main']['temp'] - 273.15)}°C" \
                  f"\nWind 🌬 -- {res['wind']['speed']}m/s" \
                  f"\nPercentage of cloudiness -- {res['clouds']['all']}%"
            await message.answer(txt)
        except KeyError:
            await message.answer("Something went wrong, could you try again later")
        except TypeError:
            await message.answer("Something went wrong, could you try again later")
        # Instead, using try except, I used to use dict.get('smt') which will return None for not consisting Key


async def get_Currency(message: types.Message, state: FSMContext):
    log(message.from_id, '__Currency__', message.text)
    # getting entities
    entities = message.text.split('-')
    # filtering entities
    for e in entities:
        ind = entities.index(e)
        entities.remove(e)
        e = e.rstrip()
        e = e.lstrip()
        e = e.upper()
        entities.insert(ind, e)
    try:
        res = get_currency(entities[1], entities[2])  # Requesting
        # Cause of CF free only restricts to use direct currency exchange we use base currency
        # to get rates from (It is dollar)
        cur_in_base = int(entities[0]) / float(
            '%.2f' % float(res.get('rates').get(entities[1].upper())))  # Amount in USD
        cur_in_need = cur_in_base * float(
            '%.2f' % float(res.get('rates').get(entities[2].upper())))  # Amount in Needed Currency
        await message.answer(
            f"Current rate: {entities[0]} {entities[1]} ~ %0.2f {entities[2]}" % cur_in_need
        )
    except IndexError:
        await message.answer("Something went wrong, could you try again later")
    except KeyError:
        await message.answer("Something went wrong, could you try again later")
    except TypeError:
        await message.answer("Something went wrong, could you try again later")
