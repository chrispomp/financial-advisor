"""Charting analyst agent."""

from google.adk.agents import LlmAgent
from financial_advisor.config import MODEL
from . import prompt

# This is a placeholder for your charting tool.
# You will need to implement this tool based on your charting library of choice.
def create_chart(data: str, chart_type: str) -> str:
    """Creates a chart with the given data and chart type."""
    return f"Chart of type {chart_type} with data {data} created."


charting_analyst = LlmAgent(
    name="charting_analyst",
    model=MODEL,
    description="Use this agent to generate charts and graphs.",
    instruction=prompt.CHARTING_ANALYST_PROMPT,
    tools=[create_chart],
)