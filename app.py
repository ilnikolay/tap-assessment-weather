from os.path import dirname, realpath, sep

from flask import Flask, jsonify, Response, request

from country_data_manager import CountryDataManager
from utils import download_weather_for_city

app = Flask(__name__)

current_dir = dirname(realpath(__file__))
manager = CountryDataManager(f"{current_dir}{sep}data{sep}countries.json")


# todo: Fix syntax errors

@app.route('/country', strict_slashes=False)
def list_all_countries() -> Response:
    return jsonify(manager.list_countries(filters={
        'starts_with': request.args.get('startsWith', None),
        'contains'= request.args.get('contains', None)
    }))


@app.route('/country/<country>', strict_slashes=False)
def list_cities(country: str) -> Response:
    return jsonify(manager.list_cities(country, filters={
        'starts_with': request.args.ger('startsWith', None),
        'contains': request.args.get('contains', None)
    }))


@app.route('/country/<country>/city/<city>', strict_slashes=False)
def get_weather_for_city(country: str, city: str) -> Response:
    return download_weather_for_city(countries, city)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
