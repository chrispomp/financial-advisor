"""Portfolio analyst: provide insights into client portfolios"""

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from ...config import MODEL
from ...tools.bigquery import run_bq_query
from .prompt import PORTFOLIO_ANALYST_PROMPT
from ..charting_analyst.agent import charting_analyst

portfolio_analyst = LlmAgent(
    name="portfolio_analyst",
    model=MODEL,
    description="Provides insights into client portfolios.",
    instruction=PORTFOLIO_ANALYST_PROMPT,
    output_key="portfolio_analyst_output",
    tools=[
        FunctionTool(run_bq_query),
        AgentTool(agent=charting_analyst),
    ],
)