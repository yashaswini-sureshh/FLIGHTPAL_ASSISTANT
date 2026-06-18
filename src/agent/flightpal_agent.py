from src.agent.planner import create_plan
from src.agent.executor import execute_plan
from src.agent.agent_router import run_agent
from src.agent.context import resolve_query
from src.agent.memory import save_memory


def flightpal(query):

    resolved_query = resolve_query(query)

    plan = create_plan(query)

    print("PLAN:", plan)

    if len(plan) > 1:

        try:

            flight_no = query.split()[-1].upper()

            response = execute_plan(
                plan,
                flight_no
            )

        except Exception as e:

            response = f"Planner Error: {e}"

    else:

        response = run_agent(resolved_query)

    save_memory(
        query,
        response
    )

    return response