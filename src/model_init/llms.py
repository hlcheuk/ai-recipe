import os
from dotenv import load_dotenv
from langchain_core.runnables import ConfigurableField
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI, AzureChatOpenAI

# from langchain_google_vertexai import ChatVertexAI

from src.utils.utils import read_yaml

# Load environment variables from .env file
load_dotenv(override=True)

# Load config from llms.yaml
llms_config = read_yaml("config/setting.yaml")["llms"]

# Get model config for Github models
github_config = llms_config["github"]
gpt_4o_mini_config = github_config["gpt-4o-mini"]
gpt_4o_config = github_config["gpt-4o"]

# Get model config for Groq models
groq_config = llms_config["groq"]
llama31_config = groq_config["llama-3.1-70b"]
llama3_config = groq_config["llama-3-70b"]

# Get model config for yi-01 models
yi01_config = llms_config["yi-01"]
yi_large_config = yi01_config["yi-large"]
yi_large_turbo_config = yi01_config["yi-large-turbo"]
yi_spark_config = yi01_config["yi-spark"]

# Get model config for deepseek models
deepseek_config = llms_config["deepseek"]
deepseek_chat_config = deepseek_config["deepseek-chat"]

# Get model config for Google models
# google_config = llms_config["google"]
# gemini_15_pro_config = google_config["gemini-1.5-pro"]
# gemini_15_flash_config = google_config["gemini-1.5-flash"]

llm_gpt_4o_mini = ChatOpenAI(
    model=gpt_4o_mini_config["model_name"],
    openai_api_base=os.getenv("GITHUB_ENDPOINT"),
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    max_tokens=gpt_4o_mini_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)

llm_gpt_4o = ChatOpenAI(
    model=gpt_4o_config["model_name"],
    openai_api_base=os.getenv("GITHUB_ENDPOINT"),
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    max_tokens=gpt_4o_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)

llm_llama31 = ChatGroq(
    model_name=llama31_config["model_name"],
    max_tokens=llama31_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    )
)

llm_llama3 = ChatGroq(
    model_name=llama3_config["model_name"],
    max_tokens=llama3_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    )
)

llm_yi_large = ChatOpenAI(
    model=yi_large_config["model_name"],
    openai_api_base="https://api.lingyiwanwu.com/v1",
    openai_api_key=os.getenv("YI_API_KEY"),
    max_tokens=yi_large_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)


llm_yi_large_turbo = ChatOpenAI(
    model=yi_large_turbo_config["model_name"],
    openai_api_base="https://api.lingyiwanwu.com/v1",
    openai_api_key=os.getenv("YI_API_KEY"),
    max_tokens=yi_large_turbo_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)

llm_yi_spark = ChatOpenAI(
    model=yi_spark_config["model_name"],
    openai_api_base="https://api.lingyiwanwu.com/v1",
    openai_api_key=os.getenv("YI_API_KEY"),
    max_tokens=yi_spark_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)

llm_deepseek_chat = ChatOpenAI(
    model=deepseek_chat_config["model_name"],
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    openai_api_base="https://api.deepseek.com",
    max_tokens=deepseek_chat_config["max_tokens"],
).configurable_fields(
    temperature=ConfigurableField(
        id="temperature",
        name="LLM Temperature",
        description="The temperature of the LLM",
    ),
    top_p=ConfigurableField(
        id="top_p",
        name="Top P of LLM",
        description="The top p of the LLM",
    ),
)

# llm_gemini_15_pro = ChatVertexAI(
#     project=gemini_15_pro_config["project_id"],
#     model_name=gemini_15_pro_config["model_name"],
#     max_tokens=gemini_15_pro_config["max_tokens"],
# )

# llm_gemini_15_flash = ChatVertexAI(
#     project=gemini_15_flash_config["project_id"],
#     model_name=gemini_15_flash_config["model_name"],
#     max_tokens=gemini_15_flash_config["max_tokens"],
# )
