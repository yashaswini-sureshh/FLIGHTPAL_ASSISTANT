from .flight_api import get_flight_status
from .weather_api import get_weather


def get_flight_weather(flight_number):

    flight = get_flight_status(flight_number)

    if isinstance(flight, str):
        return flight

    arrival_airport = flight["arrival_airport"]

    weather = get_weather(arrival_airport)

    return {
        "flight": flight,
        "weather": weather
    }