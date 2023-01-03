from dataclasses import dataclass

from rdw_explorer.property.property import Property


@dataclass
class Vehicle:

    properties: dict[str, Property]

    def __str__(self) -> str:
        plate = self.properties['kenteken']
        brand = self.properties.get('merk', None)
        model = self.properties.get('handelsbenaming', None)

        string = f"{plate.value}: {brand.value if brand else '?'} {model.value if model else '?'}"

        return string

    def __repr__(self) -> str:
        return str(self)
