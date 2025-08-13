"""Tool to query BigQuery."""
import logging
import os
import sys
from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError
import pandas as pd

# --- 1. Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


class BigQueryError(Exception):
    """Custom exception for BigQuery errors."""


def run_bq_query(query: str) -> str:
    """
    Executes a standard SQL query against Google BigQuery.

    Args:
        query: The BigQuery SQL query string to be executed.

    Returns:
        A string containing the query results in JSON format or a detailed error message.

    Raises:
        BigQueryError: If the Google Cloud Project ID is not configured.
    """
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        raise BigQueryError("Google Cloud Project ID is not configured.")
    try:
        client = bigquery.Client(project=project_id)
        logger.info(f"[Tool] Executing BigQuery query: {query}")
        query_job = client.query(query)
        results_df = query_job.to_dataframe()

        if results_df.empty:
            return "The query executed successfully but returned no data."

        # Convert to JSON and return
        results_json = results_df.to_json(orient="records", indent=2)
        logger.info(f"[Tool] Query returned {len(results_df)} records.")
        return results_json

    except GoogleCloudError as e:
        error_message = f"BigQuery API Error: {e}"
        logger.error(f"[Tool Error] {error_message}")
        return error_message
    except Exception as e:
        error_message = f"An unexpected error occurred during BigQuery execution: {e}"
        logger.error(f"[Tool Error] {error_message}")
        return error_message