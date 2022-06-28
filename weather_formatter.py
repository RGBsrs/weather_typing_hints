from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """
    Format the weather data into a string
    """
    
    return(
        f"""
        Current weather in {weather.city}
        Temperature: {weather.temperature}
        Conditions: {weather.weather_type.value}
        sunrise: {weather.sunrise}
        sunset: {weather.sunset}
        """
    )