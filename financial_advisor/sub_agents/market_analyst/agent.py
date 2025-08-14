"""Market analyst: provide insights into the financial markets"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool # <-- Import AgentTool
from ...config import MODEL
from .prompt import MARKET_ANALYST_PROMPT
from ..charting_analyst.agent import charting_analyst # <-- Import the charting_analyst

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description="Provides insights into the financial markets.",
    instruction=MARKET_ANALYST_PROMPT,
    output_key="market_analyst_output",
    tools=[
        AgentTool(agent=charting_analyst) # <-- Add the charting_analyst as a tool
    ],
)