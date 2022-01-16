from typing import Dict, List
import json
from requests import get

WEATHER_API_URL = 'https://goweather.herokuapp.com/weather'


def load_countries_from_file(filename: str) -> Dict[str, List[str]]:
    with open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def download_weather_for_city(country: str, city: str):
    response = get(f"{WEATHER_API_URL}/{city},{country}")

    if response.status_code == 200:
        return response.json()

    raise ConnectionError('Weather API is not available.')
