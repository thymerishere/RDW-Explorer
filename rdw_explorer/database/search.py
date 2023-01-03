from dataclasses import dataclass
from enum import Enum

from rdw_explorer.config import Config
from rdw_explorer.database import query_factory
from rdw_explorer.database.connection import SodaConnection
from rdw_explorer.property import property_factory
from rdw_explorer.property.property import Property
from rdw_explorer.vehicle import Vehicle


class SearchResult:
    
    list[Vehicle]


class Search:
    
    _connection: SodaConnection
    _gekentekende_voertuigen_api: str
    _gekentekende_voertuigen_brandstof_api: str

    def __init__(self, config: Config) -> None:
        self._connection = SodaConnection(config)
        self._gekentekende_voertuigen_api = config.gekentekende_voertuigen_api
        self._gekentekende_voertuigen_brandstof_api = config.gekentekende_voertuigen_brandstof_api
        
    @staticmethod
    def _json_to_vehicle(obj: dict[str, str]) -> Vehicle:
        properties = [property_factory.from_field(field, value) for field, value in obj.items()]
        property_dict = {property.field: property for property in properties}
        vehicle = Vehicle(property_dict)
        return vehicle

    def search(self, vehicle: Vehicle) -> list[Vehicle]:
        query = query_factory.from_vehicle(vehicle)
        url = self._gekentekende_voertuigen_api + query
        vehicle_jsons = self._connection.query_request(url)
        vehicles = [self._json_to_vehicle(vehicle_json) for vehicle_json in vehicle_jsons]
        return vehicles
