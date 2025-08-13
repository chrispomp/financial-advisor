"""Tool to perform a Google search."""
import os
from googleapiclient.discovery import build
from google.adk.tools import FunctionTool

@FunctionTool
def google_search(query: str) -> str:
    """
    Performs a Google search and returns the top results.

    Args:
        query: The search query.

    Returns:
        A string containing the search results.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    cse_id = os.environ.get("CUSTOM_SEARCH_ENGINE_ID")

    if not api_key or not cse_id:
        return "Error: Google API Key or Custom Search Engine ID is not configured."

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=5).execute()
        
        if "items" not in res:
            return "No results found for your query."
            
        snippets = [item.get("snippet", "") for item in res.get("items", [])]
        return "\n".join(snippets)
    except Exception as e:
        return f"An error occurred during Google search: {e}"