from src.router.llm_router import route_with_llm
from src.agent.tool_registry import TOOLS
from src.agent.memory import (
    set_last_flight
)


def run_agent(query):

    decision = route_with_llm(query)

    tool = decision.tool
    args = decision.args

    if args is None:
        args = {}

    print("\nDECISION:")
    print(decision)

    print("\nARGS:")
    print(args)

    print("\nTOOL SELECTED:")
    print(tool)

    try:

        if tool not in TOOLS:
            return f"Tool not found: {tool}"

        # WEATHER TOOL
        if tool == "weather":

            location = args.get("location")

            if not location:
                return "Weather tool requires a location."

            return TOOLS[tool](location)

        # FLIGHT STATUS TOOL
        if tool == "flight_status":

            flight_number = args.get(
                "flight_number"
            )

            if not flight_number:
                return "Flight status tool requires a flight number."

            set_last_flight(
                flight_number
            )

            return TOOLS[tool](
                flight_number
            )

        # FLIGHT WEATHER TOOL
        if tool == "flight_weather":

            flight_number = args.get(
                "flight_number"
            )

            if not flight_number:
                return "Flight weather tool requires a flight number."

            set_last_flight(
                flight_number
            )

            return TOOLS[tool](
                flight_number
            )

        # RAG TOOL
        if tool == "rag":

            print("CALLING RAG TOOL")

            query_text = args.get(
                "query",
                query
            )

            result = TOOLS[tool](
                query_text
            )

            print("RAG RESULT:")
            print(result)

            return result

        return f"Unsupported tool: {tool}"

    except Exception as e:

        print("\nERROR:")
        print(str(e))

        return f"Tool Error: {str(e)}"