from src.tools.flight_tool import (
    flight_tool
)

from src.tools.weather_tool import (
    weather_tool
)

from src.tools.rag_tool import (
    rag_tool
)

from src.tools.flight_weather_tool import (
    flight_weather_tool
)


def route_query(query):

    query_lower = query.lower()

    if "weather in" in query_lower:

        city = query_lower.replace(
            "weather in",
            ""
        ).strip()

        return weather_tool(city)

    if "flight weather" in query_lower:

        flight_no = query.split()[-1].upper()

        return flight_weather_tool(
            flight_no
        )

    if "flight status" in query_lower:

        flight_no = query.split()[-1].upper()

        return flight_tool(
            flight_no
        )

    return rag_tool(query)