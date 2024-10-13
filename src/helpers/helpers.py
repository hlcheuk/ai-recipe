from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles

from src.model_init.llms import (
    llm_gpt_4o_mini,
    llm_gpt_4o,
    llm_yi_large,
    llm_yi_large_turbo,
    llm_yi_spark,
)
from src.utils.utils import read_yaml

# Load config from setting.toml
setting_config = read_yaml("config/setting.yaml")

# Get model config for Groq modelsW
chains_config = setting_config["chains"]
intent_config = chains_config["intent"]
cusine_config = chains_config["cusine"]


def define_llm(config: dict):
    """
    Defines a Large Language Model (LLM) based on the provided configuration.

    Args:
        config (dict): A dictionary containing the LLM configuration.
            It should have the following keys:
                - llm (str): The type of LLM to define. Can be "yi-large", "yi-large-turbo", or "llama-3.1-70b".
                - temperature (float): The temperature of the LLM.
                - top_p (float): The top p of the LLM.

    Returns:
        LLM: The defined Large Language Model.
    """
    if config["llm"] == "gpt-4o-mini":
        llm = llm_gpt_4o_mini
    elif config["llm"] == "gpt-4o":
        llm = llm_gpt_4o
    elif config["llm"] == "yi-large":
        llm = llm_yi_large
    elif config["llm"] == "yi-large-turbo":
        llm = llm_yi_large_turbo
    elif config["llm"] == "yi-spark":
        llm = llm_yi_spark
    llm = llm.with_config(
        configurable={
            "temperature": config["temperature"],
            "top_p": config["top_p"],
        }
    )
    return llm


def visualise_runnable(runnable):
    """
    Visualises a graph from the provided application.

    Args:
        runnable: The application containing the graph to be visualised.

    Returns:
        None
    """
    runnable.get_graph().draw_mermaid_png(
        draw_method=MermaidDrawMethod.API,
        curve_style=CurveStyle.NATURAL,
        output_file_path="visualisation/graph.png",
    )


if __name__ == "__main__":
    define_llm()
    visualise_runnable()
