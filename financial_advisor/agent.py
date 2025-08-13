"""Financial advisor: provide reasonable investment strategies"""
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from . import prompts # UPDATED IMPORT
from . import tools

MODEL = "gemini-2.5-flash"

# Root agent that acts as a router to the sub-agents
root_agent = LlmAgent(
    name="financial_advisor",
    model=MODEL,
    description=(
        "A financial advisor that can provide market analysis and data visualizations."
    ),
    instruction=prompts.FINANCIAL_ADVISOR_PROMPT, # UPDATED REFERENCE
    tools=[
        google_search,
        tools.plot_stock_prices_tool,
    ],
    enable_planning=True,
)