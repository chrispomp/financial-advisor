"""market_analyst_agent for finding information using google search"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-flash"

market_analyst_agent = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description=(
        "Provides comprehensive and timely financial market information. "
        "Generates 'Daily Briefings' and 'Market Roundups', and answers "
        "specific user questions using Google Search."
    ),
    instruction=prompt.MARKET_ANALYST_PROMPT,
    output_key="market_data_analysis_output",
    tools=[google_search],
)
