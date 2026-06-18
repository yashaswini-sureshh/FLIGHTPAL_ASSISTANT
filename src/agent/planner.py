# src/agent/planner.py

def create_plan(query):

    query = query.lower()

    plan = []

    travel_words = [
        "travel",
        "trip",
        "flight",
        "airport",
        "journey"
    ]

    weather_words = [
        "weather",
        "temperature",
        "rain",
        "jacket"
    ]

    if any(word in query for word in travel_words):
        plan.append("flight")

    if any(word in query for word in weather_words):
        plan.append("weather")

    return plan