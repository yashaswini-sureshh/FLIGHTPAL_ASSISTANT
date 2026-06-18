from src.api.flight_api import get_flight_status
from src.api.weather_api import get_weather


def execute_plan(plan, flight_no):

    context = {}

    for step in plan:

        if step == "flight_status":

            result = get_flight_status(
                flight_no
            )

            if isinstance(result, str):
                return result

            context["flight"] = result

        elif step == "weather":

            if "flight" not in context:
                return "Flight information unavailable."

            flight = context["flight"]

            if "arrival_airport" not in flight:
                return "Arrival airport not available."

            airport = flight["arrival_airport"]

            result = get_weather(
                airport
            )

            context["weather"] = result

    return context