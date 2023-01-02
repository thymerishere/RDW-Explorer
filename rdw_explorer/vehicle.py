from dataclasses import dataclass

from rdw_explorer.property.property import Property


@dataclass
class Vehicle:

    properties: list[Property]
