

from dataclasses import dataclass
from typing import Generic, TypeVar
from rdw_explorer.property.property import Property


T = TypeVar('T')


class BasicProperty(Property, Generic[T]):

    _field: str
    _value: T
    _name: str

    def __init__(self, field: str, value: T, name: str) -> None:
        self._field = field
        self._value = value
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> T:
        return self._value

    @property
    def field(self) -> str:
        return self._field
