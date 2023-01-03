

from dataclasses import dataclass
from typing import Generic, TypeVar
from rdw_explorer.property.property import Property


T = TypeVar('T')


class BasicProperty(Property, Generic[T]):

    _name: str
    _value: T
    _field: str

    def __init__(self, name: str, value: T, field: str) -> None:
        self._name = name
        self._value = value
        self._field = field

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> T:
        return self._value

    @property
    def field(self) -> str:
        return self._field
