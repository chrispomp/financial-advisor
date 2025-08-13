"""Portfolio analyst agent."""

from google.adk.agents import LlmAgent
from financial_advisor.config import MODEL
from financial_advisor.tools.bigquery import run_bq_query
from . import prompt

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description=(
        "Use this agent for specific client portfolio information, holdings, and personalized recommendations."
    ),
    instruction=prompt.PORTFOLIO_ANALYST_PROMPT,
    tools=[run_bq_query],
)