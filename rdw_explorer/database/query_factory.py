from collections.abc import Sequence
from rdw_explorer.property.property import Property

def from_args(args: dict[str, str]):
    query_elements = [_query_element_from_arg(field, value) for field, value in args.items()]
    query = f"?$where={' and '.join(query_elements)}"
    return query

def _query_element_from_arg(field: str, value: str) -> str:
    if field == 'kenteken':
        f'{field} like "{value}"'
    return f'{field} like "%{value}%"'
