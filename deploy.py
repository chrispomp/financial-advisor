# deploy.py

import vertexai
from vertexai.preview import reasoning_engines
from market_analyst.main import market_analyst_agent

# --- Configuration ---
# Your specific GCP environment details have been added here.
PROJECT_ID = "fsi-banking-agentspace"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://fsi-banking-agentspace-adk-staging"

def deploy_agent():
    """
    Initializes Vertex AI, wraps the ADK agent in an AdkApp,
    and deploys it to Agent Engine.
    """
    # [cite_start]Initialize Vertex AI with your project details [cite: 3350-3354]
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET,
    )

    # [cite_start]Wrap your agent in an AdkApp to make it deployable [cite: 3416-3419]
    # enable_tracing=True is recommended for debugging and monitoring.
    app = reasoning_engines.AdkApp(
        agent=market_analyst_agent,
        enable_tracing=True,
    )

    # [cite_start]Deploy the AdkApp to Agent Engine [cite: 3450-3454]
    # This process can take several minutes.
    remote_app = reasoning_engines.create(
        agent_engine=app,
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]",
            # Add any other specific libraries your agent needs here
        ]
    )

    print(f"🎉 Agent deployed successfully!")
    print(f"Resource Name: {remote_app.resource_name}")

if __name__ == "__main__":
    deploy_agent()