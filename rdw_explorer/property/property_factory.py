
from rdw_explorer.property.basic_property import BasicProperty
from rdw_explorer.property.plate import Plate
from rdw_explorer.property.property import Property


def from_field(field: str, value: str) -> Property:
    if field == 'kenteken':
        return Plate('Kenteken', value, field)
    return BasicProperty(field, value, field)

