from os.path import dirname, realpath, sep

import pytest

from country_data_manager import CountryDataManager
from utils import load_countries_from_file, download_weather_for_city, WEATHER_API_URL

TEST_FILE_PATH = f"{dirname(realpath(__file__))}{sep}data{sep}test_countries.json"


def test_intialize_data_from_file():
    data = load_countries_from_file(TEST_FILE_PATH)

    # Assert types
    assert isinstance(data, dict)
    assert isinstance(list(data.keys())[0], str)
    assert isinstance(data.get('Afghanistan'), list)
    assert isinstance(data.get('Afghanistan')[0], str)

    # Assert number of elements
    assert len(data) == 3
    assert len(data.get('Afghanistan')) == 4


def test_list_countries_without_filters():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries()

    assert len(countries) == 3
    assert countries[0] == 'Afghanistan'


def test_list_countries_with_starts_with_filters():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries(filters={'starts_with': 'Al'})

    assert len(countries) == 2
    assert 'Albania' in countries
    assert 'Algeria' in countries


def test_list_countries_with_starts_with_filters_ignores_case():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries(filters={'starts_with': 'al'})

    assert len(countries) == 2
    assert 'Albania' in countries
    assert 'Algeria' in countries


def test_list_countries_with_contains_filter():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries(filters={'contains': 'ia'})

    assert len(countries) == 2
    assert 'Albania' in countries
    assert 'Algeria' in countries


def test_list_countries_with_contains_filter_ignores_case():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries(filters={'contains': 'AN'})

    assert len(countries) == 2
    assert 'Afghanistan' in countries
    assert 'Albania' in countries


def test_list_countries_with_filters_in_conjunction():
    manager = CountryDataManager(TEST_FILE_PATH)

    countries = manager.list_countries(filters={'starts_with': 'Al', 'contains': 'AN'})

    assert len(countries) == 1
    assert 'Albania' in countries


def test_list_cities_without_filters():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan')

    assert len(cities) == 4
    assert cities[0] == 'Herat'


def test_list_cities_with_starts_with_filters():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan', filters={'starts_with': 'Sha'})

    assert len(cities) == 2
    assert 'Shar' in cities
    assert 'Sharif' in cities


def test_list_cities_with_starts_with_filters_ignores_case():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan', filters={'starts_with': 'sha'})

    assert len(cities) == 2
    assert 'Shar' in cities
    assert 'Sharif' in cities


def test_list_cities_with_contains_filter():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan', filters={'contains': 'ha'})

    assert len(cities) == 2
    assert 'Shar' in cities
    assert 'Sharif' in cities


def test_list_cities_with_contains_filter_ignores_case():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan', filters={'contains': 'h'})

    assert len(cities) == 4
    assert 'Herat' in cities
    assert 'Molah' in cities
    assert 'Shar' in cities
    assert 'Sharif' in cities


def test_list_cities_with_filters_in_conjunction():
    manager = CountryDataManager(TEST_FILE_PATH)

    cities = manager.list_cities('Afghanistan', filters={'starts_with': 'sha', 'contains': 'ari'})

    assert len(cities) == 1
    assert 'Sharif' in cities


def test_weather_api_with_success(requests_mock):
    requests_mock.get(f"{WEATHER_API_URL}/Budapest,Hungary", status_code=200, json={
        'temperature': '',
        'forecast': ''
    })

    weather = download_weather_for_city('Hungary', 'Budapest')

    assert 'temperature' in weather
    assert 'forecast' in weather


def test_weather_api_with_server_error(requests_mock):
    requests_mock.get(f"{WEATHER_API_URL}/Budapest,Hungary", status_code=500)

    with pytest.raises(ConnectionError):
        download_weather_for_city('Hungary', 'Budapest')


def test_e2e_weather_api():
    weather = download_weather_for_city('Hungary', 'Budapest')

    assert 'temperature' in weather
    assert 'forecast' in weather
