# src/agent/memory.py

chat_history = []

last_flight = None
last_city = None


def save_memory(user_message, assistant_response):

    chat_history.append(
        {
            "user": user_message,
            "assistant": str(assistant_response)
        }
    )

    if len(chat_history) > 10:
        chat_history.pop(0)


def get_memory():
    return chat_history


def get_context():

    context = ""

    for item in chat_history[-5:]:

        context += f"""
User: {item['user']}
Assistant: {item['assistant']}
"""

    return context


def set_last_flight(flight_number):

    global last_flight

    last_flight = flight_number


def get_last_flight():

    return last_flight


def set_last_city(city):

    global last_city

    last_city = city


def get_last_city():

    return last_city