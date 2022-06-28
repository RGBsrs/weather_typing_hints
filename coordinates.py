from typing import NamedTuple


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

def get_coordinates() -> Coordinates:
    """
    Get the coordinates from the user.
    """

    longitude = 50.4546600
    latitude = 30.5238000

    return Coordinates(longitude=longitude, latitude=latitude)

if __name__ == "__main__":
    print(get_coordinates())