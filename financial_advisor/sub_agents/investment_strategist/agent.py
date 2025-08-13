"""investment_strategist_agent for developing holistic investment/trading strategies"""

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-flash"

investment_strategist_agent = LlmAgent(
    name="investment_strategist",
    model=MODEL,
    description=(
        "Helps develop holistic investment/trading strategies, including "
        "trading strategy generation, execution planning, and risk analysis."
    ),
    instruction=prompt.INVESTMENT_STRATEGIST_PROMPT,
    output_key="investment_strategist_output",
)
