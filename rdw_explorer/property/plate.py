from dataclasses import dataclass
from enum import Enum

from rdw_explorer.property.property import Property


class PlateCharType(Enum):

    N = int
    L = str
    S = str


class Plate(Property):

    _name: str
    _value: str
    _field: str
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

    def __init__(self, name: str, value: str, field: str) -> None:
        self._name = name
        self._value = value
        self._field = field
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
