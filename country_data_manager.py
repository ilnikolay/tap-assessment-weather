from typing import List, Dict, Optional

from utils import load_countries_from_file


class CountryDataManager:
    def __init__(self, filename: str) -> None:
        self._data = load_countries_from_file(filename)

    def list_countries(self, filters: Dict[str, Optional[str]] = None) -> List[str]:
        # todo: implement getting countries from self._data with filtering, ignore case, see tests.py and README.md
        #  for more details
        pass

    def list_cities(self, country: str, filters: Dict[str, Optional[str]] = None) -> List[str]:
        # todo: implement getting cities for a country from self._data with filtering, ignore case, see tests.py and
        #  README.md for more details
        pass
