

from dataclasses import dataclass
from typing import Generic, TypeVar
from rdw_explorer.property.property import Property


T = TypeVar('T')


@dataclass
class BasicProperty(Property, Generic[T]):

    name: str
    value: T
    field: str

