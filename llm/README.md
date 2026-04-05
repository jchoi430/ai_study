# Basic LLM Example

This directory contains a basic example of how to use Google's Generative AI SDK to interact with the Gemini models.

## Files

- `basic_llm.py`: A simple Python script that connects to the `gemini-2.5-flash` model and asks it to generate a short poem about Python programming.

## Prerequisites

1.  **Install dependencies:** Ensure you have the required packages installed according to the project's setup (e.g., via `pip install google-generativeai` or `poetry install`/`uv sync` depending on your `pyproject.toml`).
2.  **Set your API Key:** The script requires a valid Google Gemini API key. You must set it as an environment variable named `GOOGLE_API_KEY`. You can set this in your environment or defined in the `.env` file.

    ```bash
    export GOOGLE_API_KEY="your_api_key_here"
    ```

## Usage

To execute the script and see the generated response, run:

```bash
python basic_llm.py
```
