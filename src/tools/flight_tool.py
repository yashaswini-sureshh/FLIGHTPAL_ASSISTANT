from src.api.flight_api import get_flight_status


def run(flight_number):

    return get_flight_status(
        flight_number
    )