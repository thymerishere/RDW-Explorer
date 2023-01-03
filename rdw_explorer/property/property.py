from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Property(ABC, Generic[T]):

    @property
    @abstractmethod
    def name(self) -> str:
        """Written name of this property."""

    @property
    @abstractmethod
    def value(self) -> T:
        """Value of this property."""

    @property
    @abstractmethod
    def field(self) -> str:
        """Name of this property as found in the database."""

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"

    def __repr__(self) -> str:
        return str(self)
