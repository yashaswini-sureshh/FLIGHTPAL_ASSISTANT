from src.tools.weather_tool import run as weather
from src.tools.flight_tool import run as flight_status
from src.tools.flight_weather_tool import run as flight_weather
from src.tools.rag_tool import run as rag


TOOLS = {
    "weather": weather,
    "flight_status": flight_status,
    "flight_weather": flight_weather,
    "rag": rag
}


def execute_tool(tool_name, tool_input):

    if tool_name not in TOOLS:
        return "Tool not found"

    return TOOLS[tool_name](tool_input)