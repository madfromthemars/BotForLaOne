# Request lib
import requests
from requests import exceptions

API_URL = "82fcadd87b36b795c2802b02c760c443"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


# Get Weather By City
def owmByCity(city, lang='en'):
    res = None
    try:
        res = requests.get(BASE_URL + f'q={city}&appid={API_URL}&lang={lang}', ).json()
        return res
    except exceptions.ConnectionError:
        print("Problem with Connection OWM-Location")
    except exceptions.HTTPError:
        print("Invalid Http Response OWM-Location")
    except exceptions.Timeout:
        print("Request Timeout OWM-Location")
    except:
        print("Unknown Problem with OWM-Location")


# Get Weather By Location
def owmByLocation(lat, lon, lang='en'):
    res = None
    try:
        res = requests.get(BASE_URL + f'lat={lat}&lon={lon}&appid={API_URL}&lang={lang}').json()
        return res
    except exceptions.ConnectionError:
        print("Problem with Connection OWM-Location")
    except exceptions.HTTPError:
        print("Invalid Http Response OWM-Location")
    except exceptions.Timeout:
        print("Request Timeout OWM-Location")
    except:
        print("Unknown Problem with OWM-Location")
