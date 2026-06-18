# src/agent/context.py

from src.agent.memory import get_context


def resolve_query(query):

    memory_context = get_context()

    return f"""
Previous Conversation:

{memory_context}

Current User Query:

{query}
"""