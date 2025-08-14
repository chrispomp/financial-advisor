"""Market analyst: provide insights into the financial markets"""

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from ...config import MODEL
from ...tools.google_search import google_search
from .prompt import MARKET_ANALYST_PROMPT
from ..charting_analyst.agent import charting_analyst

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description="Provides insights into the financial markets.",
    instruction=MARKET_ANALYST_PROMPT,
    output_key="market_analyst_output",
    tools=[
        FunctionTool(google_search),
        AgentTool(agent=charting_analyst),
    ],
)