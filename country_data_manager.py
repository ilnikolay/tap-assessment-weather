from typing import List, Dict, Optional

from utils import load_countries_from_file


class CountryDataManager:
    def __init__(self, filename: str) -> None:
        self._data = load_countries_from_file(filename)

    def list_countries(self, filters: Dict[str, Optional[str]] = None) -> List[str]:
        # todo: implement getting countries from self._data with filtering, ignore case, see tests.py and README.md
        #  for more details

        filtered_output = []
        if filters == None:
            for country_name in self._data:
                filtered_output.append(country_name)
        else:
            for country_name in self._data:
                for filters_key, key_value in filters.items():
                    if filters_key == 'contains' and key_value.lower() in country_name.lower():
                        filtered_output.append(country_name)
                    if filters_key == 'starts_with' and country_name.lower().startswith(key_value.lower()):
                        filtered_output.append(country_name)
        return filtered_output



    def list_cities(self, country: str, filters: Dict[str, Optional[str]] = None) -> List[str]:
        # todo: implement getting cities for a country from self._data with filtering, ignore case, see tests.py and
        #  README.md for more details
        pass
