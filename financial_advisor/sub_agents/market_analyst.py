"""Sub-agent for market analysis"""
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from financial_advisor import prompts

MODEL = "gemini-2.5-flash"

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Use this agent for market analysis, investment strategies, daily briefings, "
        "or market roundups. This agent can search for financial information."
    ),
    instruction=prompts.MARKET_ANALYST_PROMPT,
    tools=[google_search],
)