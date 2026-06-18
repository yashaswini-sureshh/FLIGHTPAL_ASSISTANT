import os

from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from .vector_store import get_retriever

load_dotenv()

retriever = get_retriever()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

def ask_flightpal(question):

    question_lower = question.lower().strip()

    if question_lower in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]:
        return """
Hello! 👋

I'm FlightPal, your AI travel assistant.

I can help with:

✈ Flight status
🌦 Weather
🛄 Baggage rules
🏢 Airport information
📄 Travel documents

What would you like to know?
"""

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are FlightPal.
    respond to greatings if user greets to you as a flightpal

    Use ONLY the provided context.

    If the answer is not present in the context,
    say:
    "I could not find that information."

    Context:
    {context}

    Question:
    {question}
    """
    try:
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"LLM Error: {str(e)}"