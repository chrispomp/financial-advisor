"""Market analyst: provide insights into the financial markets"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from ...config import MODEL
from .prompt import MARKET_ANALYST_PROMPT

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description="Provides insights into the financial markets.",
    instruction=MARKET_ANALYST_PROMPT,
    output_key="market_analyst_output",
    tools=[
        google_search,
    ],
)