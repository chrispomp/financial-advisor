"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt
from . import charting

MODEL = "gemini-2.5-flash"

# Sub-agent for market analysis
market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Use this agent for market analysis, investment strategies, daily briefings, "
        "or market roundups. This agent can search for financial information."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    tools=[google_search],
)

# Sub-agent for creating charts
data_visualization = LlmAgent(
    name="data_visualization",
    model=MODEL,
    description="Use this agent to generate a line chart or plot of stock prices.",
    instruction=prompt.DATA_VISUALIZATION_PROMPT,
    tools=[charting.plot_stock_prices],
)

# Root agent that acts as a router to the sub-agents
# This agent has NO tools of its own, only sub-agents.
root_agent = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A financial advisor that can provide market analysis and data visualizations."
    ),
    instruction=prompt.FINANCIAL_ADVISOR_PROMPT,
    sub_agents=[
        market_analyst,
        data_visualization,
    ],
)