"""Market analyst agent."""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from financial_advisor.config import MODEL
from financial_advisor.tools.charting import charting
from . import prompt

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Guides users through a structured process to receive financial "
        "advice. Helps them analyze a market ticker and develop holistic "
        "investment/trading strategies."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    output_key="market_analyst_output",
    tools=[
        google_search,
        charting,
    ],
)