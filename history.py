from datetime import datetime
from pathlib import Path

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage:
    """
    Interface for a weather storage
    """

    def save_weather(self, weather: Weather) -> None:
        raise NotImplementedError()


class PlainFileWeatherStorage(WeatherStorage):
    """
    Stores weather data in a plain text file
    """

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def save_weather(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self.file_path, 'a') as f:
            f.write(f"{now}\n{formatted_weather}\n")

