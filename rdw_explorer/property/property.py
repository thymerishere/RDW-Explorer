from abc import ABC, abstractmethod


class Property(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """Written name of this property."""

    @property
    @abstractmethod
    def value(self) -> str:
        """Value of this property."""

    @property
    @abstractmethod
    def field(self) -> str:
        """Name of this property as found in the database."""
