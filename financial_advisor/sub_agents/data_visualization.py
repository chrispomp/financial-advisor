"""Sub-agent for data visualization."""
from google.adk.agents import LlmAgent
from financial_advisor import prompts
from financial_advisor import tools

MODEL = "gemini-2.5-flash"

data_visualization = LlmAgent(
    name="data_visualization",
    model=MODEL,
    description="Use this agent to generate a line chart or plot of stock prices.",
    instruction=prompts.DATA_VISUALIZATION_PROMPT,
    tools=[tools.plot_stock_prices_tool],
)