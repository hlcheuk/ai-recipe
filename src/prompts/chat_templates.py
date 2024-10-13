from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.prompts.prompts import (
    INTENT_INSTRUCTION,
    INTENT_PROMPT,
    CHITCHAT_INSTRUCTION,
    CHITCHAT_PROMPT,
    CUSINE_INSTRUCTION,
    CUSINE_PROMPT,
    INTRO_INSTRUCTION,
    INTRO_PROMPT,
    NEED_FOR_RECIPE_INSTRUCTION,
    NEED_FOR_RECIPE_PROMPT,
    NEED_FOR_OTHER_HELP_INSTRUCTION,
    NEED_FOR_OTHER_HELP_PROMPT,
    WRITE_RECIPE_INSTRUCTION,
    WRITE_RECIPE_PROMPT,
    DETECT_RECIPE_NEED_INSTRUCTION,
    DETECT_RECIPE_NEED_PROMPT,
)
from src.prompts.few_shots import (
    intent_examples,
    cusine_examples,
    detect_recipe_need_examples,
)
from src.utils.utils import read_yaml

# Load config from setting.toml
setting_config = read_yaml("config/setting.yaml")

# Get model config for Groq models
chains_config = setting_config["chains"]
cusine_config = chains_config["cusine"]

intent_template = ChatPromptTemplate.from_messages(
    [
        ("system", INTENT_INSTRUCTION),
        *intent_examples,
        ("user", INTENT_PROMPT),
    ]
)

chitchat_template = ChatPromptTemplate.from_messages(
    [
        ("system", CHITCHAT_INSTRUCTION),
        MessagesPlaceholder(variable_name="messages"),
        ("user", CHITCHAT_PROMPT),
    ]
)

cusine_template = ChatPromptTemplate.from_messages(
    [
        ("system", CUSINE_INSTRUCTION),
        *cusine_examples,
        ("user", CUSINE_PROMPT),
    ]
).partial(no_of_cusine=cusine_config["no_of_cusine"])

intro_template = ChatPromptTemplate.from_messages(
    [
        ("system", INTRO_INSTRUCTION),
        ("user", INTRO_PROMPT),
    ]
)

need_for_recipe_template = ChatPromptTemplate.from_messages(
    [
        ("system", NEED_FOR_RECIPE_INSTRUCTION),
        ("user", NEED_FOR_RECIPE_PROMPT),
    ]
)

need_for_other_help_template = ChatPromptTemplate.from_messages(
    [
        ("system", NEED_FOR_OTHER_HELP_INSTRUCTION),
        ("user", NEED_FOR_OTHER_HELP_PROMPT),
    ]
)

write_recipe_template = ChatPromptTemplate.from_messages(
    [
        ("system", WRITE_RECIPE_INSTRUCTION),
        ("user", WRITE_RECIPE_PROMPT),
    ]
)

detect_recipe_need_template = ChatPromptTemplate.from_messages(
    [
        ("system", DETECT_RECIPE_NEED_INSTRUCTION),
        *detect_recipe_need_examples,
        # MessagesPlaceholder(variable_name="last_message"),
        ("user", DETECT_RECIPE_NEED_PROMPT),
    ]
)
