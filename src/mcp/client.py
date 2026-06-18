from src.mcp.server import execute_tool


def call_tool(tool_name, tool_input):

    return execute_tool(
        tool_name,
        tool_input
    )