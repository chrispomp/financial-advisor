"""Financial advisor: provide reasonable investment strategies"""
from google.adk.agents import LlmAgent
from . import sub_agents
from . import prompts # UPDATED IMPORT

MODEL = "gemini-2.5-flash"

# Root agent that acts as a router to the sub-agents
root_agent = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A financial advisor that can provide market analysis and data visualizations."
    ),
    instruction=prompts.FINANCIAL_ADVISOR_PROMPT, # UPDATED REFERENCE
    sub_agents=[
        sub_agents.market_analyst,
        sub_agents.data_visualization,
    ],
)