from typing import List, Dict, Optional

from utils import load_countries_from_file


class CountryDataManager:
    def __init__(self, filename: str) -> None:
        self._data = load_countries_from_file(filename)

    @staticmethod
    def filt_func(filters, c_name: str):
        if filters is None or not any(filters.values()):
            return True
        if all(filters.values()) and len(filters) == 2:
            if filters['contains'].lower() in c_name.lower() and \
                c_name.lower().startswith(filters['starts_with'].lower()):
                return True
        else:
            try:
                return bool(filters['contains'].lower() in c_name.lower())
            except (KeyError, AttributeError):
                return bool(c_name.lower().startswith(filters['starts_with'].lower()))
        return False

    def list_countries(self, filters: Dict[str, Optional[str]] = None) -> List[str]:
        filtered_output = [country for country in self._data if self.filt_func(filters,country)]
        return filtered_output

    def list_cities(self, country: str, filters: Dict[str, Optional[str]] = None) -> List[str]:
        for country_name, cities in self._data.items():
            if country_name == country:
                city_list = [city for city in cities if self.filt_func(filters,city)]
        return city_list
