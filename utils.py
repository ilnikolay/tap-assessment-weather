from typing import Dict, List

from requests import get

WEATHER_API_URL = 'https://goweather.herokuapp.com/weather'


def load_countries_from_file(filename: str) -> Dict[str, List[str]]:
    # todo: Read a json file into a dictionary of cities, where the keys are the country names,
    #  and their values are their cities. See tests.py for details.
    pass


def download_weather_for_city(country: str, city: str):
    response = get(f"{WEATHER_API_URL}/{city},{country}")

    if response.status_code == 200:
        return response.json()

    raise ConnectionError('Weather API is not available.')
