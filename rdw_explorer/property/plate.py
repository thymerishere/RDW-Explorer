from dataclasses import dataclass
from enum import Enum

class PlateCharType(Enum):

    N = int
    L = str
    S = str

@dataclass
class Plate(Property):

    format: list[PlateCharType]
    chars: list[str]

    @property
    def value(self) -> str:

