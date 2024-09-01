import random
from langchain_core.messages import HumanMessage, AIMessage

from src.prompts.prompts import INTENT_PROMPT, CUSINE_PROMPT, PICK_INGREDIENTS_PROMPT
from src.tools.tools import get_available_ingredients
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

ingredients = get_available_ingredients()
no_of_cusine = cusine_config["no_of_cusine"]
cusine_examples = ["梅菜扣肉", "薑葱牛柳", "椒鹽雞翼", "清蒸鱈魚", "三杯雞"]
cusine_samples = random.sample(cusine_examples, no_of_cusine)

cusine_examples = [
    HumanMessage(
        content=CUSINE_PROMPT.format(
            ingredients=ingredients,
            extra_requirements=["中菜"],
            question="煮乜嘢好?",
            no_of_cusine=no_of_cusine,
        ),
    ),
    AIMessage(content=str(cusine_samples)),
]

pick_ingredients_examples = [
    HumanMessage(
        content=PICK_INGREDIENTS_PROMPT.format(
            cusine="意大利烤雞",
            intro="意大利烤雞係一道好味又易整嘅菜式。你只需要用雞肉，塗上意大利香料，好似羅勒、奧勒岡同蒜粉，跟手放入焗爐烤到金黃色就得。咁整出嚟嘅烤雞外皮香脆，肉質嫩滑，好開胃！",
            ingredients=ingredients,
        ),
    ),
    AIMessage(content=str(["雞胸肉去皮 400克"])),
]
