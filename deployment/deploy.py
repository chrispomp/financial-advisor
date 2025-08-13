"""Deployment script"""

import os
from typing import Any, cast
import toml

import vertexai
from absl import app, flags
from dotenv import load_dotenv
from financial_advisor.agent import root_agent
from vertexai import agent_engines
from vertexai.preview import reasoning_engines


FLAGS = flags.FLAGS
flags.DEFINE_string("project_id", None, "GCP project ID.")
flags.DEFINE_string("location", None, "GCP location.")
flags.DEFINE_string("bucket", None, "GCP bucket.")
flags.DEFINE_string("agent_engine_id", None, "The ID of the Agent Engine to update or delete.")


flags.DEFINE_bool("list", False, "List all agents.")
flags.DEFINE_bool("create", False, "Creates a new agent.")
flags.DEFINE_bool("update", False, "Updates an existing agent.")
flags.DEFINE_bool("delete", False, "Deletes an existing agent.")
flags.mark_bool_flags_as_mutual_exclusive(["create", "delete", "update", "list"])

def get_requirements():
    """Reads dependencies from pyproject.toml"""
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)
    
    dependencies = pyproject_data.get("tool", {}).get("poetry", {}).get("dependencies", {})
    
    # Filter out python dependency and format for requirements list
    requirements = [
        f"{name}{version}" for name, version in dependencies.items() if name != "python"
    ]
    return requirements

def create() -> None:
    """Creates an agent engine for Financial Advisors."""
    app = reasoning_engines.AdkApp(agent=root_agent, enable_tracing=True)

    # FINAL extra_packages LIST
    remote_agent = agent_engines.create(
        agent_engine=app,
        display_name=root_agent.name,
        requirements=get_requirements(),
        extra_packages=[
            "financial_advisor/__init__.py",
            "financial_advisor/agent.py",
            "financial_advisor/sub_agents/__init__.py",
            "financial_advisor/sub_agents/market_analyst.py",
            "financial_advisor/sub_agents/data_visualization.py",
            "financial_advisor/tools/__init__.py",
            "financial_advisor/tools/charting.py",
            "financial_advisor/prompts/__init__.py",
            "financial_advisor/prompts/root_agent.md",
            "financial_advisor/prompts/market_analyst.md",
            "financial_advisor/prompts/data_visualization.md",
        ],
    )
    print(f"Created remote agent: {remote_agent.resource_name}")


def update() -> None:
    """Updates an existing agent engine for Financial Advisors."""
    if not FLAGS.agent_engine_id:
        print("Please provide --agent_engine_id to update.")
        return

    app = reasoning_engines.AdkApp(agent=root_agent, enable_tracing=True)

    # FINAL extra_packages LIST
    updated_agent = agent_engines.update(
        resource_name=FLAGS.agent_engine_id,
        agent_engine=cast(Any, app),
        display_name=root_agent.name,
        requirements=get_requirements(),
        extra_packages=[
            "financial_advisor/__init__.py",
            "financial_advisor/agent.py",
            "financial_advisor/sub_agents/__init__.py",
            "financial_advisor/sub_agents/market_analyst.py",
            "financial_advisor/sub_agents/data_visualization.py",
            "financial_advisor/tools/__init__.py",
            "financial_advisor/tools/charting.py",
            "financial_advisor/prompts/__init__.py",
            "financial_advisor/prompts/root_agent.md",
            "financial_advisor/prompts/market_analyst.md",
            "financial_advisor/prompts/data_visualization.md",
        ],
    )
    print(f"Updated remote agent: {updated_agent.resource_name}")


def delete() -> None:
    """Deletes an existing agent engine for Financial Advisors."""
    if not FLAGS.agent_engine_id:
        print("Please provide --agent_engine_id to delete.")
        return
        
    remote_agent = agent_engines.get(FLAGS.agent_engine_id)
    remote_agent.delete(force=True)
    print(f"Deleted remote agent: {FLAGS.agent_engine_id}")


def list_agents() -> None:
    remote_agents = agent_engines.list()
    template = """
{agent.name} ("{agent.display_name}")
- Create time: {agent.create_time}
- Update time: {agent.update_time}
"""
    remote_agents_string = "\n".join(
        template.format(agent=agent) for agent in remote_agents
    )
    print(f"All remote agents:\n{remote_agents_string}")


def main(argv: list[str]) -> None:
    del argv  # unused
    load_dotenv()

    project_id = (
        FLAGS.project_id
        if FLAGS.project_id
        else os.getenv("GOOGLE_CLOUD_PROJECT")
    )
    location = (
        FLAGS.location if FLAGS.location else os.getenv("GOOGLE_CLOUD_LOCATION")
    )
    bucket = (
        FLAGS.bucket
        if FLAGS.bucket
        else os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
    )

    print(f"PROJECT: {project_id}")
    print(f"LOCATION: {location}")
    print(f"BUCKET: {bucket}")

    if not project_id:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        return
    elif not location:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        return
    elif not bucket:
        print(
            "Missing required environment variable: GOOGLE_CLOUD_STORAGE_BUCKET"
        )
        return

    vertexai.init(
        project=project_id,
        location=location,
        staging_bucket=f"gs://{bucket}",
    )

    if FLAGS.list:
        list_agents()
    elif FLAGS.create:
        create()
    elif FLAGS.update:
        update()
    elif FLAGS.delete:
        delete()
    else:
        print("Unknown command. Please use --list, --create, --update, or --delete.")


if __name__ == "__main__":
    app.run(main)