from datetime import datetime
from enum import Enum
from typing import NamedTuple

from .coordinates import Coordinates


Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"

class Weather(NamedTuple):
    """
    The weather for a given location.
    """

    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """
    Get the weather for the given coordinates.
    """

    return Weather(
        temperature=10,
        weather_type=WeatherType.THUNDERSTORM,
        sunrise=datetime.now(),
        sunset=datetime.now(),
        city="Kyiv"
    )