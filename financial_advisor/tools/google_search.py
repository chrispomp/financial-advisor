"""Tool to perform Google searches."""
import os
from googleapiclient.discovery import build

def google_search(query: str) -> str:
    """
    Performs a Google search using the Custom Search JSON API.

    Args:
        query: The search query.

    Returns:
        A string containing the search results or an error message.
    """
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        cse_id = os.environ.get("GOOGLE_CSE_ID")

        if not api_key or not cse_id:
            return "Google API key or CSE ID is not configured."

        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=5).execute()

        if 'items' not in res:
            return "No results found."

        # Format the results
        formatted_results = []
        for item in res['items']:
            formatted_results.append(f"Title: {item['title']}\\nLink: {item['link']}\\nSnippet: {item['snippet']}\\n")

        return "\\n".join(formatted_results)

    except Exception as e:
        return f"An error occurred during Google search: {e}"
