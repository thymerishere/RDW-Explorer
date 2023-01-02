from rdw_explorer.vehicle import Vehicle


def from_vehicle(vehicle: Vehicle) -> str:
    query_elements = [
        _create_query(property.field, property.value)
        for property in vehicle.properties
    ]

    if not query_elements:
        return ""

    query = f"$where {' and '.join(query_elements)}"
    return query


def _create_query(field: str, value: str, exact: bool = True) -> str:
    value_str = value
    if exact:
        value_str = f".*{value_str}.*"
    result = f"={field} like {value_str}"
    return result

