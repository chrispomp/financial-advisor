"""Charting analyst agent."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from financial_advisor.config import MODEL
from . import prompt

# Import the other sub-agents to use them as tools
from financial_advisor.sub_agents.market_analyst.agent import market_analyst
from financial_advisor.sub_agents.portfolio_analyst.agent import portfolio_analyst

charting_analyst = LlmAgent(
    name="charting_analyst",
    model=MODEL,
    description="Generates charts and graphs based on financial data. Routes requests to other agents to retrieve the necessary information.",
    instruction=prompt.CHARTING_ANALYST_PROMPT,
    tools=[
        AgentTool(agent=market_analyst),
        AgentTool(agent=portfolio_analyst),
    ],
)