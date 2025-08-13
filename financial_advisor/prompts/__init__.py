"""Loads prompts from markdown files."""
import os

def _load_prompt(file_name: str) -> str:
    """Loads a prompt from a file in the current directory."""
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, file_name), "r") as f:
        return f.read()

FINANCIAL_ADVISOR_PROMPT = _load_prompt("root_agent.md")
MARKET_ANALYST_PROMPT = _load_prompt("market_analyst.md")
DATA_VISUALIZATION_PROMPT = _load_prompt("data_visualization.md")