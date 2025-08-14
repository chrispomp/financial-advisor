"""Charting analyst agent."""

from google.adk.agents import LlmAgent
from financial_advisor.config import MODEL
from financial_advisor.tools.charting import charting
from . import prompt

charting_analyst = LlmAgent(
    name="charting_analyst",
    model=MODEL,
    description="Generates charts and graphs based on financial data.",
    instruction=prompt.CHARTING_ANALYST_PROMPT,
    tools=[
        charting,
    ],
)