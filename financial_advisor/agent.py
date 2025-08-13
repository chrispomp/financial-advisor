"""Financial advisor: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent

from .sub_agents import market_analyst, portfolio_analyst

MODEL = "gemini-2.5-flash"

FINANCIAL_ADVISOR_PROMPT = """
You are a router. Your only job is to analyze the user's query and transfer control to the most appropriate sub-agent based on its description. Do not try to answer the question yourself.

- If the user asks for financial market insights, economic trends, or business news, transfer to the `market_analyst`.
- If the user asks for specific client portfolio information, holdings, or personalized recommendations, transfer to the `portfolio_analyst`.

You must only select one sub-agent to transfer to.
"""

financial_advisor = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A router agent that directs user queries to the appropriate sub-agent."
    ),
    instruction=FINANCIAL_ADVISOR_PROMPT,
    sub_agents=[market_analyst, portfolio_analyst],
)

root_agent = financial_advisor