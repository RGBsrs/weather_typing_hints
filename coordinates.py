from typing import NamedTuple


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

def get_coordinates() -> Coordinates:
    """
    Get the coordinates from the user.
    """
    return Coordinates(longitude=0.0, latitude=0.0)