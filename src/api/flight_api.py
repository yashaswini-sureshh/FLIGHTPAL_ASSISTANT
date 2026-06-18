import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def get_flight_status(flight_number):

    url = (
        f"http://api.aviationstack.com/v1/flights"
        f"?access_key={API_KEY}"
        f"&flight_iata={flight_number}"
    )

    response = requests.get(url)

    data = response.json()

    print("\nAPI RESPONSE:")
    print(data)

    if "error" in data:
        return data["error"]["message"]

    if len(data.get("data", [])) == 0:
        return "Flight not found"

    flight = data["data"][0]

    return {
        "flight": flight_number,
        "status": flight["flight_status"],
        "airline": flight["airline"]["name"],
        "departure_airport": flight["departure"]["airport"],
        "arrival_airport": flight["arrival"]["airport"],
        "departure_gate": flight["departure"]["gate"],
        "arrival_gate": flight["arrival"]["gate"],
        "arrival_delay": flight["arrival"]["delay"]
    }