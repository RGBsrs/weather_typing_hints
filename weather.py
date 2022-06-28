from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from history import save_weather

def main():
    coordinates = get_coordinates()
    weather = get_weather(coordinates)
    print(format_weather(weather))

if __name__ == "__main__":
    main()