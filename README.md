

# AI Recipe Chatbot

## Project Overview

This project is a conversational AI system designed to assist users with cooking-related tasks. It leverages the power of LLM and agentic workflow to provide cusine recipes with reference. This project is built with the framework `LangGraph` and utilise Google Search as tool.

## Demo

This project is deployed on GCP. You may visit [here](https://ai-recipe-483285956947.asia-east2.run.app/) to give this chatbot a try. Please note that it may take a few minutes to cold start.

Here's a quick demonstration of how to use the AI Recipe Chatbot:

Starting a conversation:
![Starting a conversation](docs/demo.gif)

## Features

* Recipe search and generation
* Cooking instructions and guidance
* Conversational interface for user interaction
* Integration with external APIs for recipe data and search functionality

## Technical Details

* Built using Python 3.11 and various libraries (see `requirements.txt`)
* Utilizes the `LangGraph` library for conversational AI functionality
* Integrates with Google Search API for recipe search functionality
* Uses YAML configuration files (`config/setting.yaml`) for models and chains configuration

## Project Structure

```
ai-recipe/
│
├── app.py                 # Streamlit Web UI for the conversational AI system
├── graph.py               # Core architecture of the graph structure and logic
├── src/
│   ├── model_init/        # Model initialization and configuration files
│   ├── state/             # State definitions of the graph
│   ├── prompts/           # Prompt templates and examples for conversational AI
│   ├── chains/            # Chain definitions for Langgraph nodes
│   ├── tools/             # Tool definitions for the node to use
│   ├── utils/             # Utility functions for the project
│   ├── helpers/           # Helper functions for the project
│   └── docs/     	       # Animated GIF for demo purpose
│
├── docs/                  # Animated GIF for demo purpose
├── visualisation/         # Graph structure visualisation
│
├── config/
│   └── setting.yaml       # Configuration file for models and chains
│
└── requirements.txt       # List of project dependencies
```


## Getting Started

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/hlcheuk/ai-recipe.git
   cd ai-recipe
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to `http://localhost:8501` to interact with the AI Recipe Chatbot.


## Roadmap

We're constantly working to improve the AI Recipe Chatbot. Here are some features and improvements we're planning to implement:

1. Streaming output: Provide token-by-token responses as the graph generates them, creating a more interactive experience with faster response time.

2. LLM selection: Provide a panel for users to choose between different LLMs.

## Acknowledgments

* Thanks to the creators of LangGraph for providing a powerful tool for building conversational AI systems.
