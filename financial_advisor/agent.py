"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt
from . import charting

MODEL = "gemini-2.5-flash"


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
    ],
)

data_visualization = LlmAgent(
    name="data_visualization",
    model=MODEL,
    description=(
        "Generates a line chart of stock prices."
    ),
    instruction="Generate a line chart of stock prices.",
    output_key="data_visualization_output",
    tools=[
        charting.plot_stock_prices,
    ],
)

root_agent = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A financial advisor that can provide market analysis and data visualizations."
    ),
    instruction=(
        "You are a financial advisor. If the user asks for market analysis or "
        "investment strategies, use the 'market_analyst' tool. If the user asks for a "
        "chart or plot of stock prices, use the 'data_visualization' tool."
    ),
    sub_agents=[
        market_analyst,
        data_visualization,
    ]
)