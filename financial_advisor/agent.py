"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt
from .tools.bigquery import run_bq_query

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

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description=(
        "Use this agent for specific client portfolio information, holdings, and personalized recommendations."
    ),
    instruction=prompt.PORTFOLIO_ANALYST_PROMPT,
    tools=[run_bq_query],
)


# This is now a "pure" router agent with NO tools of its own.
financial_advisor = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A router agent that directs user queries to the appropriate sub-agent."
    ),
    instruction=prompt.FINANCIAL_ADVISOR_PROMPT,
    sub_agents=[market_analyst, portfolio_analyst],
)

root_agent = financial_advisor