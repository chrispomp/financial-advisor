"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent, RouterAgent
from google.adk.tools import google_search

from . import prompt
from .tools.bigquery import run_bq_query

MODEL = "gemini-2.5-flash"

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Retrieves financial market insights, economic trends/news, business"
        " news, etc. using google_search."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    tools=[
        google_search,
    ],
)

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description=(
        "Retrieves client information from BigQuery to serve up personalized"
        " insights and recommendations."
    ),
    instruction=prompt.PORTFOLIO_ANALYST_PROMPT,
    tools=[
        run_bq_query,
    ],
)


financial_advisor = RouterAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "The direct contact point with the user, and will use the sub agents to"
        " perform specific tasks."
    ),
    instruction=prompt.FINANCIAL_ADVISOR_PROMPT,
    agents=[market_analyst, portfolio_analyst],
)

root_agent = financial_advisor