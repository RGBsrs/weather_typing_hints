from datetime import datetime
from enum import Enum
from typing import Literal, NamedTuple, Union

from dotenv import dotenv_values
import requests

from coordinates import Coordinates
from exeptions import APIServiceError


config = dotenv_values()

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

    openweathether_response = _get_openweather_response(
        latitude=coordinates.latitude, longitude=coordinates.longitude
    )
    weather = _parse_openweather_response(openweathether_response)
    return weather

def _get_openweather_response(latitude: float = 0, longitude: float = 0) -> dict:
    """
    Get the response from the OpenWeather API.
    """
    API_URL = f"""https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&units=metric&appid={config['OPEN_WEATHER_API_KEY']}"""
    try:
        response = requests.get(API_URL)
    except requests.exceptions.RequestException:
        raise APIServiceError("Invalid response from OpenWeather API.")
    if response.status_code != 200:
        raise APIServiceError(response.status_code)
    else:
        return response.json()

def _parse_openweather_response(response: dict) -> Weather:
    """
    Parse the response from the OpenWeather API.
    """
    weather_type = _parse_weather_type(response)
    temperature = _parse_temperature(response)
    sunrise = _parse_sun_time(response, "sunrise")
    sunset = _parse_sun_time(response, "sunset")
    city = "Kyiv"
    return Weather(
        temperature=temperature,
        weather_type=weather_type,
        sunrise=sunrise,
        sunset=sunset,
        city=city,
    )

def _parse_temperature (response: dict) -> Celsius:
    """
    Parse the temperature from the OpenWeather API response.
    """

    return response["current"]["temp"]

def _parse_weather_type(response: dict) -> WeatherType:
    """
    Parse the weather type from the OpenWeather API response.
    """

    try:
        wether_type_id = response["current"]["weather"][0]["id"]
    except (IndexError, KeyError):
        raise APIServiceError("Invalid response from OpenWeather API.")
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS,
    }
    for _id, weather_type in weather_types.items():
        if str(wether_type_id).startswith(_id):
            return weather_type
    raise APIServiceError("Invalid response from OpenWeather API.")

def _parse_sun_time(
    response: dict,
    time: Union[Literal["sunrise"], Literal["sunset"]]) -> datetime:
    """
    Parse the sunrise from the OpenWeather API response.
    """

    return datetime.fromtimestamp(response["current"][time])

if __name__ == "__main__":
    print(get_weather(Coordinates(longitude=30.52, latitude=50.45)))