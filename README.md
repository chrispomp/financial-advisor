# Financial Advisor


## Overview

The Financial Advisor is a team of specialized AI agents that assists human financial advisors.

1. Data Analyst Agent: This agent is responsible for creating in-depth and current market analysis reports for specific stock tickers. It achieves this by repeatedly using Google Search to find a predetermined amount of unique, recent (within a given timeframe), and insightful information. The agent focuses on gathering both SEC filings and broader market intelligence via Google Search tool, which it then uses to compile a structured report based solely on the collected data.

2. Trading Analyst Agent: This agent's task is to develop and describe at least five different trading strategies. It does this by carefully reviewing the comprehensive market analysis provided by the Data Analyst Agent. Each proposed strategy must be customized to match the user's declared risk tolerance and intended investment duration.

3. Execution Agent: This agent creates a thorough and well-justified plan for implementing a given trading strategy. The plan must be carefully adjusted to fit the user's risk tolerance, investment timeframe, and preferred methods of execution. The output will be detailed and fact-based, examining the best approaches and specific timing for initiating, maintaining, adding to, partially selling, and completely exiting investment positions.

4. Risk Evaluation Agent: This agent's role is to produce a detailed and reasoned analysis of the risks associated with a specific trading strategy and its execution plan. This analysis needs to be precisely aligned with the user's stated risk tolerance, investment period, and execution preferences. The output will be rich in factual analysis, clearly outlining all identified risks and suggesting concrete, actionable steps to lessen their impact.

## Agent Details

The key features of the Financial Advisor include:

| Feature | Description |
| --- | --- |
| **Interaction Type** | Conversational |
| **Complexity**  | Medium |
| **Agent Type**  | Multi Agent |
| **Components**  | Tools: built-in Google Search |
| **Vertical**  | Financial |


### Agent architecture:

This diagram shows the detailed architecture of the agents and tools used
to implement this workflow.
<img src="financial-advisor.png" alt="Financial Advisor" width="800"/>

## Setup and Installation

1.  **Prerequisites**

    *   Python 3.11+
    *   Poetry
        *   For dependency management and packaging. Please follow the
            instructions on the official
            [Poetry website](https://python-poetry.org/docs/) for installation.

        ```bash
        pip install poetry
        ```

    * A project on Google Cloud Platform
    * Google Cloud CLI
        *   For installation, please follow the instruction on the official
            [Google Cloud website](https://cloud.google.com/sdk/docs/install).

2.  **Installation**

    ```bash
    # Clone this repository.
    git clone https://github.com/google/adk-samples.git
    cd adk-samples/python/agents/financial_advisor
    # Install the package and dependencies.
    poetry install
    ```

3.  **Configuration**

    *   Set up Google Cloud credentials.

        *   You may set the following environment variables in your shell, or in
            a `.env` file instead.

        ```bash
        export GOOGLE_GENAI_USE_VERTEXAI=true
        export GOOGLE_CLOUD_PROJECT=fsi-banking-agentspace
        export GOOGLE_CLOUD_LOCATION=us-central1
        export GOOGLE_CLOUD_STORAGE_BUCKET=fsi-banking-agentspace-adk-staging
        ```

    *   Authenticate your GCloud account.

        ```bash
        gcloud auth application-default login
        gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
        ```

## Running the Agent

**Using `adk`**

ADK provides convenient ways to bring up agents locally and interact with them.
You may talk to the agent using the CLI:

```bash
adk run financial_advisor
```

Or on a web interface:

```bash
 adk web
```


## Running Tests

For running tests and evaluation, install the extra dependencies:

```bash
poetry install --with dev
```

Then the tests and evaluation can be run from the `financial-advisor` directory using
the `pytest` module:

```bash
python3 -m pytest tests
python3 -m pytest eval
```

`tests` runs the agent on a sample request, and makes sure that every component
is functional. `eval` is a demonstration of how to evaluate the agent, using the
`AgentEvaluator` in ADK. It sends a couple requests to the agent and expects
that the agent's responses match a pre-defined response reasonably well.


## Deployment

The Financial Advisor can be deployed to Vertex AI Agent Engine using the following
commands:

```bash
poetry install --with deployment
python3 deployment/deploy.py --create
```

When the deployment finishes, it will print a line like this:

```
Created remote agent: projects/<PROJECT_NUMBER>/locations/<PROJECT_LOCATION>/reasoningEngines/<AGENT_ENGINE_ID>
```

If you forgot the AGENT_ENGINE_ID, you can list existing agents using:

```bash
python3 deployment/deploy.py --list
```

The output will be like:

```
All remote agents:

123456789 ("financial_advisor")
- Create time: 2025-05-12 12:35:34.245431+00:00
- Update time: 2025-05-12 12:36:01.421432+00:00
```

You may interact with the deployed agent using the `test_deployment.py` script
```bash
$ export USER_ID=<any string>
$ python3 deployment/test_deployment.py --resource_id=${AGENT_ENGINE_ID} --user_id=${USER_ID}
Found agent with resource ID: ...
Created session for user ID: ...
Type 'quit' to exit.
Input: Hello, what can you do for me?
Response: Hello! I can guide you through a structured process to receive financial advice. We'll work together with a team of expert subagents to:

1.  **Analyze a market ticker**: We'll start by having you provide a market ticker symbol (e.g., AAPL, GOOGL). Our data analyst subagent will then provide a comprehensive analysis of it.
2.  **Develop trading strategies**: Based on the market analysis and your risk attitude and investment period, our trading strategist subagent will propose potential trading strategies.
3.  **Define an execution plan**: Next, our execution specialist subagent will create a detailed plan for implementing the chosen strategy, considering factors like order types and timing.
4.  **Evaluate the overall risk**: Finally, our risk analyst subagent will assess the overall risk of the financial plan, ensuring it aligns with your goals and risk tolerance.

Would you like to begin by providing a market ticker symbol for analysis?
```

To delete the deployed agent, you may run the following command:

```bash
python3 deployment/deploy.py --delete --resource_id=${AGENT_ENGINE_ID}
```

