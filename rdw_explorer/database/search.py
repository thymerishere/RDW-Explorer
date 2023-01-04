from dataclasses import dataclass, field
import pandas as pd

from rdw_explorer.config import Config
from rdw_explorer.database import query_factory
from rdw_explorer.database.connection import SodaConnection, SodaMetadata
from rdw_explorer.property import property_factory
from rdw_explorer.property.property import Property
from rdw_explorer.vehicle import Vehicle


@dataclass
class SearchResult:

    vehicles: pd.DataFrame = field(default_factory=lambda: pd.DataFrame())

    def union(self, other: 'SearchResult') -> 'SearchResult':
        if self.vehicles.empty or other.vehicles.empty:
            return SearchResult()

        vehicles = pd.merge(
            self.vehicles,
            other.vehicles,
            how='inner',
            left_on='kenteken',
            right_on='kenteken',
        )

        return SearchResult(vehicles)

    @staticmethod
    def from_json(obj: list[dict[str, str]]) -> 'SearchResult':
        search_result = SearchResult(pd.DataFrame(obj))
        return search_result

    def __str__(self) -> str:
        if self.vehicles.empty:
            return "SearchResult(Empty)"

        return str(self.vehicles[['kenteken', 'merk', 'handelsbenaming', 'eerste_kleur']])


class Search:
    
    _connection: SodaConnection
    _gekentekende_voertuigen_api: str
    _gekentekende_voertuigen_brandstof_api: str
    _gekentekende_voertuigen_metadata: SodaMetadata
    _gekentekende_voertuigen_brandstof_metadata: SodaMetadata

    def __init__(self, config: Config) -> None:
        self._connection = SodaConnection(config)
        self._gekentekende_voertuigen_api = config.gekentekende_voertuigen_api
        self._gekentekende_voertuigen_brandstof_api = config.gekentekende_voertuigen_brandstof_api
        self._gekentekende_voertuigen_metadata = (
            self._connection.get_metadata(self._gekentekende_voertuigen_api)
        )
        self._gekentekende_voertuigen_brandstof_metadata = (
            self._connection.get_metadata(self._gekentekende_voertuigen_brandstof_api)
        )

    def filter_args(self, args: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
        args = {arg: value for arg, value in args.items() if value is not None}

        non_brandstof_fields = [field.name 
                                for field in self._gekentekende_voertuigen_metadata.fields]
        non_brandstof_args = {field: value for field, value in args.items() 
                              if field in non_brandstof_fields}

        brandstof_fields = [field.name 
                            for field in self._gekentekende_voertuigen_brandstof_metadata.fields]
        brandstof_args = {field: value for field, value in args.items() 
                          if field in brandstof_fields}

        return non_brandstof_args, brandstof_args

    def _get_from_url(self, url: str) -> SearchResult:
        vehicle_jsons = self._connection.query_request(url)
        search_result = SearchResult.from_json(vehicle_jsons)
        return search_result

    def dict_search(self, args: dict[str, str]) -> SearchResult:
        non_brandstof_args, brandstof_args = self.filter_args(args)
        search_result = None

        if non_brandstof_args:
            query = query_factory.from_args(non_brandstof_args)
            url = self._gekentekende_voertuigen_api + query
            search_result = self._get_from_url(url)
        if brandstof_args:
            query = query_factory.from_args(brandstof_args)
            url = self._gekentekende_voertuigen_brandstof_api + query
            if search_result is not None:
                search_result = search_result.union(self._get_from_url(url))
            else:
                search_result = self._get_from_url(url)

        return search_result or SearchResult()
