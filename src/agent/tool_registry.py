from src.api.weather_api import get_weather
from src.api.flight_api import get_flight_status
from src.api.flight_weather import get_flight_weather

from src.tools.rag_tool import rag_tool


TOOLS = {
    "weather": get_weather,
    "flight_status": get_flight_status,
    "flight_weather": get_flight_weather,
    "rag": rag_tool
}