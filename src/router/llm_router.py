import os
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load environment variables safely
load_dotenv()

# 2. Define the exact output structure using Pydantic
class RoutingDecision(BaseModel):
    """Decide which tool to route the user query to."""
    tool: Literal["weather", "flight_status", "flight_weather", "rag"] = Field(
        description="The name of the tool to use."
    )
    args: Dict[str, Any] = Field(
        default_factory=dict,
        description="The extracted arguments/parameters needed for the tool."
    )

# 3. Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# 4. Bind the schema to the model natively
structured_llm = llm.with_structured_output(RoutingDecision)

def route_with_llm(query: str) -> RoutingDecision:
    """Routes the user query to the appropriate tool using structured outputs."""
    
    # Notice we removed the JSON formatting examples from the prompt.
    # The Pydantic schema handles the structure under the hood automatically.
    system_prompt = (
        "You are a routing agent. Analyze the user query and select the best "
        "available tool to handle the request. Extract any necessary arguments."
    )
    
    # Combine system instructions and user query into a clean message list
    messages = [
        ("system", system_prompt),
        ("human", query)
    ]
    
    try:
        # Returns a native RoutingDecision object directly
        decision = structured_llm.invoke(messages)
        return decision
        
    except Exception as e:
        # Fallback safety layer in case API or validation fails
        print(f"Routing failed due to error: {e}")
        return RoutingDecision(tool="rag", args={"query": query})

# Example Usage:
if __name__ == "__main__":
    result = route_with_llm("What is the weather like in New York?")
    
    # You can access properties cleanly as an object or dictionary
    print(f"Selected Tool: {result.tool}")
    print(f"Arguments: {result.args}")
    print(f"As Dictionary: {result.model_dump()}")
