import random
from langchain_core.messages import HumanMessage, AIMessage

from src.prompts.prompts import (
    INTENT_PROMPT,
    CUSINE_PROMPT,
    DETECT_RECIPE_NEED_PROMPT,
)
from src.utils.utils import read_yaml

# Load config from setting.toml
setting_config = read_yaml("config/setting.yaml")

# Get model config for Groq models
chains_config = setting_config["chains"]
cusine_config = chains_config["cusine"]

intent_examples = [
    HumanMessage(
        content=INTENT_PROMPT.format(question="你好嗎？"),
    ),
    AIMessage(content='{"about_cusine": False, "extra_requirements": []}'),
    HumanMessage(
        content=INTENT_PROMPT.format(
            question="諗唔到今晚食乜好，有冇意大利菜介紹？唔好咁肥"
        ),
    ),
    AIMessage(
        content='{"about_cusine": True, "extra_requirements": ["意大利菜", "低脂"]}'
    ),
]

no_of_cusine = cusine_config["no_of_cusine"]
cusine_examples = ["梅菜扣肉", "薑葱牛柳", "椒鹽雞翼", "清蒸鱈魚", "三杯雞"]
cusine_samples = random.sample(cusine_examples, no_of_cusine)

cusine_examples = [
    HumanMessage(
        content=CUSINE_PROMPT.format(
            extra_requirements=["中菜"],
            question="煮乜嘢好?",
            no_of_cusine=no_of_cusine,
        ),
    ),
    AIMessage(content=str(cusine_samples)),
]

detect_recipe_need_examples = [
    HumanMessage(content="好呀"),
    AIMessage(content="yes"),
    HumanMessage(content="唔駛"),
    AIMessage(content="no"),
    HumanMessage(content="今日天氣點呀？"),
    AIMessage(content="others"),
]
