from dataclasses import dataclass
import json
from typing import Any
import requests

from rdw_explorer.config import Config
from rdw_explorer.property.property import Property


@dataclass
class SodaField:

    name: str
    type: str

@dataclass
class SodaMetadata:

    fields: list[SodaField]


class SodaConnection:

    _fields_name_in_headers: str
    _types_name_in_headers: str

    def __init__(self, config: Config) -> None:
        self._fields_name_in_headers = config.fields_name_in_headers
        self._types_name_in_headers = config.types_name_in_headers
    
    @staticmethod
    def _request(url: str):
        result = requests.get(url)
        
        if result.status_code != 200:
            raise Exception('Connection refused!')

        return result

    @staticmethod
    def _get_soda_fields_from_request(result: requests.Response) -> list[dict[str, str]]:
        assert 'json' in result.headers['content-type']
        result_json = result.json()

        assert isinstance(result_json, list)

        return result_json


    def query_request(self, url: str) -> list[dict[str, str]]:
        result = self._request(url)
        result_json = self._get_soda_fields_from_request(result)
        return result_json

    def get_metadata(self, end_point: str) -> SodaMetadata:
        query = f"{end_point}?$limit=0"
        request = self._request(query)

        fields_string = request.headers[self._fields_name_in_headers]
        names = json.loads(fields_string)

        types_string = request.headers[self._types_name_in_headers]
        types = json.loads(types_string)
        
        fields = [SodaField(name, type) for name, type in zip(names, types)] 
        
        return SodaMetadata(fields)
