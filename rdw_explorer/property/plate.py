from dataclasses import dataclass
from enum import Enum

from rdw_explorer.property.property import Property


class PlateCharType(Enum):

    N = int
    L = str
    S = str


class Plate(Property):

    _field: str
    _value: str
    _name: str
    format: list[PlateCharType]

    @staticmethod
    def _get_format(plate_string: str) -> list[PlateCharType]:
        types = []
        for char in plate_string:
            if char.isalpha():
                type_ = PlateCharType.L
            else:
                type_ = PlateCharType.N

            if types and types[-1] != type_:
                types.append(PlateCharType.S)
            
            types.append(type_)
        return types

    def __init__(self, field: str, value: str, name: str) -> None:
        self._field = field
        self._value = value
        self._name = name
        self.format = self._get_format(value)

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> str:
        return self._value

    @property
    def field(self) -> str:
        return self._field

    def query(self, _) -> str:
        return f'{self.field} like "{self.value}"' 
