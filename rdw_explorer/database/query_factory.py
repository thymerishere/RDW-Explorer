from collections.abc import Sequence
from rdw_explorer.property.property import Property


def from_properties(properties: list[Property]) -> str:
    query_elements = [
        _create_query(property.field, property.value)
        for property in properties
    ]

    if not query_elements:
        return ""

    query = f"?$where={' and '.join(query_elements)}"
    return query


def _create_query(field: str, value: str, exact: bool = True) -> str:
    value_str = value
    if exact:
        value_str = f'.*{value_str}.*'
    result = f'{field} like "{value_str}"'
    return result

