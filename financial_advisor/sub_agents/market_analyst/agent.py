"""Market analyst: provide insights into the financial markets"""

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool, google_search
from google.adk.tools.agent_tool import AgentTool
from ...config import MODEL
from .prompt import MARKET_ANALYST_PROMPT
from ..charting_analyst.agent import charting_analyst

def safe_google_search(query: str) -> str:
    """
    A safe wrapper around the built-in Google Search tool that handles exceptions.
    """
    try:
        # The built-in google_search tool is a FunctionTool object, which is callable.
        return google_search(query=query)
    except Exception as e:
        # Catch any exception and return a user-friendly error message.
        return (
            "The Google Search tool failed to execute. "
            "This might be due to a configuration issue in the cloud environment. "
            "Please check if the Custom Search API is enabled and that the service account has the correct permissions. "
            f"Error: {e}"
        )

market_analyst = LlmAgent(
    name="market_analyst",
    model=MODEL,
    description="Provides insights into the financial markets.",
    instruction=MARKET_ANALYST_PROMPT,
    output_key="market_analyst_output",
    tools=[
        FunctionTool(safe_google_search),
        AgentTool(agent=charting_analyst),
    ],
)