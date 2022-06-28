from typing import NamedTuple

from dotenv import dotenv_values


config = dotenv_values()


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

def get_coordinates() -> Coordinates:
    """
    Get the coordinates from the user.
    """

    longitude = config["LONGITUDE"]
    latitude = config["LATITUDE"]

    return Coordinates(longitude=longitude, latitude=latitude)

if __name__ == "__main__":
    print(get_coordinates())