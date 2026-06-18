import requests


def get_coordinates(location):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={location}"
        f"&count=1"
    )

    response = requests.get(url)

    data = response.json()

    if "results" not in data:
        return None

    place = data["results"][0]

    return {
        "name": place["name"],
        "country": place.get("country", ""),
        "latitude": place["latitude"],
        "longitude": place["longitude"]
    }