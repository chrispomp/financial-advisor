"""Financial coordinator: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
import asyncio

from . import prompt
from .sub_agents.market_analyst.agent import market_analyst_agent
from .sub_agents.investment_strategist.agent import investment_strategist_agent

MODEL = "gemini-2.5-flash"


financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "Guides users through a structured process to receive financial "
        "advice by orchestrating a series of expert sub-agents. Helps them "
        "analyze a market ticker and develop holistic investment/trading "
        "strategies."
    ),
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT,
    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=market_analyst_agent),
        AgentTool(agent=investment_strategist_agent),
    ],
)

async def run_in_parallel(*coroutines):
    """Executes multiple coroutines concurrently and returns their results."""
    return await asyncio.gather(*coroutines)

root_agent = financial_coordinator