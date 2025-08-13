"""Portfolio analyst agent."""

from google.adk.agents import LlmAgent

from financial_advisor.tools.bigquery import run_bq_query
from . import prompt

MODEL = "gemini-1.5-flash"

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description=(
        "Use this agent for specific client portfolio information, holdings, and personalized recommendations."
    ),
    instruction=prompt.PORTFOLIO_ANALYST_PROMPT,
    tools=[run_bq_query],
)
