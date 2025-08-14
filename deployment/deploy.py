"""Deployment script for Financial Advisor Agent Engine."""

import os
from typing import Any, cast

import vertexai
from absl import app, flags
from dotenv import load_dotenv
from financial_advisor.agent import root_agent
from google.api_core import exceptions
from vertexai import agent_engines # Correctly import the module

# --- Configuration Flags ---
FLAGS = flags.FLAGS
flags.DEFINE_string("project_id", os.getenv("GOOGLE_CLOUD_PROJECT"), "GCP project ID.")
flags.DEFINE_string("location", os.getenv("GOOGLE_CLOUD_LOCATION"), "GCP location.")
flags.DEFINE_string("bucket", os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET"), "GCP bucket for staging.")
flags.DEFINE_string("agent_id", None, "The resource name ID for an existing Agent Engine.")

# --- Action Flags ---
flags.DEFINE_bool("create", False, "Creates a new agent.")
flags.DEFINE_bool("update", False, "Updates an existing agent.")
flags.DEFINE_bool("delete", False, "Deletes an existing agent.")
flags.DEFINE_bool("list", False, "Lists all agents.")
flags.mark_bool_flags_as_mutual_exclusive(["create", "delete", "update", "list"])

# --- Agent Configurations ---
AGENT_DISPLAY_NAME = root_agent.name
AGENT_DESCRIPTION = "Financial advisor agent that provides investment strategies."
AGENT_REQUIREMENTS = [
    "google-adk>=0.1.0",
    "google-cloud-aiplatform[agent_engines]>=1.55.0",
    "google-genai>=1.0.0",
    "pydantic>=2.0.0",
    "absl-py>=2.0.0",
    "matplotlib",
    "seaborn",
    "pandas",
    "db-dtypes"
]
AGENT_EXTRA_PACKAGES = [
    "financial_advisor",
]

def create_agent() -> None:
    """Creates a new Agent Engine."""
    print("Attempting to create a new agent...")
    try:
        # 1. Call create() from the agent_engines module
        # 2. Correctly use the 'agent_engine' parameter, not 'agent'
        remote_agent = agent_engines.create(
            display_name=AGENT_DISPLAY_NAME,
            description=AGENT_DESCRIPTION,
            requirements=AGENT_REQUIREMENTS,
            extra_packages=AGENT_EXTRA_PACKAGES,
            agent_engine=root_agent,
        )
        print(f"✅ Successfully created agent: {remote_agent.resource_name}")
    except exceptions.GoogleAPICallError as e:
        print(f"❌ Error creating agent: {e}")

def update_agent(resource_name: str) -> None:
    """Updates an existing Agent Engine."""
    print(f"Attempting to update agent: {resource_name}...")
    try:
        # 1. Call update() from the agent_engines module
        # 2. Correctly use 'resource_name' and 'agent_engine' parameters
        updated_agent = agent_engines.update(
            resource_name=resource_name,
            display_name=AGENT_DISPLAY_NAME,
            description=AGENT_DESCRIPTION,
            requirements=AGENT_REQUIREMENTS,
            extra_packages=AGENT_EXTRA_PACKAGES,
            agent_engine=cast(Any, root_agent),
        )
        print(f"✅ Successfully updated agent: {updated_agent.resource_name}")
    except exceptions.NotFound:
        print(f"❌ Error: Agent with ID '{resource_name}' not found.")
    except exceptions.GoogleAPICallError as e:
        print(f"❌ Error updating agent: {e}")


def delete_agent(resource_name: str) -> None:
    """Deletes an existing Agent Engine."""
    print(f"Attempting to delete agent: {resource_name}...")
    try:
        # Call get() from the agent_engines module to fetch the agent first
        remote_agent = agent_engines.get(resource_name)
        remote_agent.delete(force=True)
        print(f"✅ Successfully deleted agent: {resource_name}")
    except exceptions.NotFound:
        print(f"❌ Error: Agent with ID '{resource_name}' not found.")
    except exceptions.GoogleAPICallError as e:
        print(f"❌ Error deleting agent: {e}")


def list_agents() -> None:
    """Lists all Agent Engines in the project."""
    print("Fetching list of agents...")
    try:
        # Call list() from the agent_engines module
        remote_agents = agent_engines.list()
        if not remote_agents:
            print("No agents found in this project/location.")
            return
        template = ('{agent.name} ("{agent.display_name}")\n'
                    '- Create time: {agent.create_time}\n'
                    '- Update time: {agent.update_time}')
        for agent in remote_agents:
            print(template.format(agent=agent))
    except exceptions.GoogleAPICallError as e:
        print(f"❌ Error listing agents: {e}")


def main(argv: list[str]) -> None:
    del argv  # Unused.
    load_dotenv()

    project_id = FLAGS.project_id
    location = FLAGS.location
    bucket = FLAGS.bucket

    if not all([project_id, location, bucket]):
        print("❌ Missing required configuration. Ensure GOOGLE_CLOUD_PROJECT, "
              "GOOGLE_CLOUD_LOCATION, and GOOGLE_CLOUD_STORAGE_BUCKET are set.")
        return

    print(f"Project: {project_id}\nLocation: {location}\nBucket: {bucket}")
    vertexai.init(project=project_id, location=location, staging_bucket=f"gs://{bucket}")

    if FLAGS.create:
        create_agent()
    elif FLAGS.update:
        if not FLAGS.agent_id:
            print("❌ --agent_id is required for update operations.")
            return
        update_agent(FLAGS.agent_id)
    elif FLAGS.delete:
        if not FLAGS.agent_id:
            print("❌ --agent_id is required for delete operations.")
            return
        delete_agent(FLAGS.agent_id)
    elif FLAGS.list:
        list_agents()
    else:
        print("No command specified. Use --create, --update, --delete, or --list.")


if __name__ == "__main__":
    app.run(main)