"""Portfolio analyst: provide insights into client portfolios"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool # <-- Import AgentTool
from ...config import MODEL
from .prompt import PORTFOLIO_ANALYST_PROMPT
from ..charting_analyst.agent import charting_analyst # <-- Import the charting_analyst

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description="Provides insights into client portfolios.",
    instruction=PORTFOLIO_ANALYST_PROMPT,
    output_key="portfolio_analyst_output",
    tools=[
        AgentTool(agent=charting_analyst) # <-- Add the charting_analyst as a tool
    ],
)