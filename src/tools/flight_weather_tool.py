from src.api.flight_weather import (
    get_flight_weather
)


def run(flight_number):

    return get_flight_weather(
        flight_number
    )