## How to use this project

To get started with this AI study repository, follow these general steps:
1. **Clone the repository** to your local machine.
2. **Install dependencies** using `uv` (e.g., `uv sync` or `uv pip install -r requirements.txt`).
3. **Configure environment variables** by creating a `.env` file based on `.env_example` and adding your necessary API keys (like `GOOGLE_API_KEY`).
4. **Run the examples** located in the individual directories (e.g., `uv run python api/basic_api.py`) to see them in action.

## How to create AI Agent in this project

Creating an AI agent involves setting up a script that leverages an LLM and gives it a specific goal or set of tools.
1. **Choose a model provider** (e.g., Google Gemini) and configure its client in your Python script.
2. **Define a system prompt** assigning a persona and providing clear instructions for what the agent should accomplish.
3. **Set up a ReAct loop** or use an existing framework to allow the agent to reason, decide on tool usage, and observe outputs.
4. **Run and evaluate** your agent's performance on the desired tasks.

## How to use skills.md

A `skills.md` file acts as the explicit instruction manual for an agent's capabilities.
1. **Create the file** in an accessible directory (e.g., inside an `agents/` folder).
2. **Write clear descriptions** of how the agent should handle specific scenarios or utilize tools, avoiding ambiguous language.
3. **Provide exact examples** of proper inputs and outputs for complex operations.
4. **Inject the file's content** into your agent's system prompt prior to execution so it learns these custom workflows dynamically.

## How to create AI Agent Plugin in this project

An AI agent plugin in this repository is designed as a modular tool or function that the agent can call.
1. **Define a Python function** with clear parameter names and type hints.
2. **Add a highly descriptive docstring**. LLMs rely almost entirely on this docstring to understand when and how to select the tool.
3. **Write the backend logic** inside the function (e.g., querying a database or an external API).
4. **Register the tool** with the agent's framework (such as passing it to the `tools=[my_function]` parameter when using the Gemini SDK).

## How to create AI Agent Plugin for Gemini, ChatGPT, or Claude

The process of formally registering a plugin varies slightly depending on the specific model platform.
1. **For Gemini:** Use Google's function calling API by passing native Python functions directly to the `tools` argument when initializing the `GenerativeModel`.
2. **For ChatGPT:** Define an OpenAPI JSON schema that details the API endpoints, parameters, and descriptions to act as a custom GPT action.
3. **For Claude:** Use Anthropic's tool-use API by providing a JSON schema with `name`, `description`, and `input_schema` properties, and explicitly handle the `tool_use` message type.

## How to use AI Agent Plugin

Using a developed plugin involves handling the execution loop between the LLM and your local machine.
1. **Prompt the Agent** asking it to perform a task that requires the plugin's capability.
2. **Listen for a tool call** response from the AI model (the model will halt response generation to return the target function name and the arguments to use).
3. **Execute the underlying code** locally by passing those arguments to the actual function or API.
4. **Return the results** (the function's output) back to the LLM so it can interpret the data, resume its thought process, and formulate its final answer.
