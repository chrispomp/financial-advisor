"""Market analyst agent."""

from google.adk.agents import LlmAgent
# Change this import to use your local google_search tool
from financial_advisor.tools.google_search import google_search

from . import prompt

MODEL = "gemini-2.5-flash"

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Use this agent for financial market insights, economic trends, and business news."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    tools=[google_search],
)