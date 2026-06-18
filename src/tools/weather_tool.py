from src.api.weather_api import get_weather


def run(location):

    return get_weather(
        location
    )