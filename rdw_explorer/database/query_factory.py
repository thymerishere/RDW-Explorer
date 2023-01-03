from collections.abc import Sequence
from rdw_explorer.property.property import Property


def from_properties(properties: list[Property]) -> str:
    query_elements = [
        property.query(False)
        for property in properties
    ]

    if not query_elements:
        return ""

    query = f"?$where={' and '.join(query_elements)}"
    return query
