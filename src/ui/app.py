import gradio as gr

from src.agent.flightpal_agent import (
    flightpal
)


def respond(message, history):

    response = flightpal(message)

    return str(response)


demo = gr.ChatInterface(
    fn=respond,
    title="✈️ FlightPal",
    description="AI Travel Assistant"
)

demo.launch(share=True)