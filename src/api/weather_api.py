import requests
from .geocoding_api import get_coordinates


def get_weather(location):

    coords = get_coordinates(location)

    if coords is None:
        return "Location not found"

    latitude = coords["latitude"]
    longitude = coords["longitude"]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    response = requests.get(url)

    data = response.json()

    current = data["current"]

    return {
        "location": coords["name"],
        "country": coords["country"],
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"]
    }