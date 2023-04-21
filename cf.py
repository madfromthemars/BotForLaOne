# || Using: Currency Freaks ||
# || Link to website: https://openweathermap.org/api ||
# || Used to -- Get Current currency ||

# Requests
import requests
from requests import exceptions

# Local
from basic import CF_TOKEN

BASE_URL = "https://api.currencyfreaks.com/v2.0/rates/latest?"


# Get Currency
def get_currency(cur_fr, cur_to):
    res = None
    try:
        res = requests.get(BASE_URL + f'apikey={CF_TOKEN}&symbols={cur_fr},{cur_to},USD').json()
        return res
    except exceptions.ConnectionError:
        print("Problem with Connection OWM-Location")
    except exceptions.HTTPError:
        print("Invalid Http Response OWM-Location")
    except exceptions.Timeout:
        print("Request Timeout OWM-Location")
    except:
        print("Unknown Problem with OWM-Location")
