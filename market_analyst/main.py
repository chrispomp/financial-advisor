# main.py

from google.adk.agents import Agent
from google.adk.tools import google_search

from . import prompt

# It's a good practice to use the latest compatible model for optimal performance.
MODEL = "gemini-2.5-flash"

# Instantiate the Agent.
# This agent is designed to act as a Market Analyst, capable of fetching
# and processing real-time financial data to produce insightful reports.
market_analyst_agent = Agent(
    model=MODEL,
    name="market_analyst",
    instruction=prompt.MARKET_ANALYST_PROMPT,
    output_key="market_data_analysis_output",
    tools=[google_search],
)