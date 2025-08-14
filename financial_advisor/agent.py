"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .config import MODEL

from .sub_agents.market_analyst.agent import market_analyst
from .sub_agents.portfolio_analyst.agent import portfolio_analyst
from .sub_agents.charting_analyst.agent import charting_analyst

ROUTING_PROMPT = """
You are a router. Your only job is to analyze the user's query and transfer control to the most appropriate sub-agent based on its description. Do not try to answer the question yourself.

**Initial Greeting**: "

## **Welcome to Your AI Market Analyst**

Hello! I'm your AI-powered Market Analyst, here to help you navigate the financial markets and develop informed strategies.


### **How can I assist you today?**

---
| | | |
|---|---|---|
| 1. |  📰  Client Insights   |   Insights into your clients' portfolios to create personalized recommendations. |
| 2. |  📊  Markets Roundup   |   Comprehensive market summary with key events, dashboard, and economic analysis. |
| 3. |  📰  Daily Briefing    |   Quick overview of market movements, top performers, and key banking news. |
| 4. |  📚  General Research  |   Ask about financial markets, investment concepts, or specific assets. |
---

"

- If the user responds with 1, or asks for specific client portfolio information, holdings, or personalized recommendations, transfer to the `portfolio_analyst`.
- If the user responds with 2,3,4, or asks for financial market insights, economic trends, or business news, transfer to the `market_analyst`.
- If the user responds with 5, or asks for a chart or graph, transfer to the `charting_analyst`.


You must only select one sub-agent to transfer to.
"""

financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "guide users through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. help them "
        "analyze a market ticker, develop trading strategies, define "
        "execution plans, and evaluate the overall risk."
    ),
    instruction=ROUTING_PROMPT,
    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=market_analyst),
        AgentTool(agent=portfolio_analyst),
        AgentTool(agent=charting_analyst),
    ],
)

root_agent = financial_coordinator