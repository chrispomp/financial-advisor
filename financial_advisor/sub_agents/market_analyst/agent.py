"""Market analyst agent."""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-1.5-flash"

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Use this agent for financial market insights, economic trends, and business news."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    tools=[google_search],
)
