from src.prompts.chat_templates import (
    intent_template,
    chitchat_template,
    cusine_template,
    intro_template,
    need_for_recipe_template,
    need_for_other_help_template,
    write_recipe_template,
)
from src.utils.utils import read_yaml
from src.helpers.helpers import define_llm

# Load config from setting.toml
setting_config = read_yaml("config/setting.yaml")

# Get model config for Groq models
chains_config = setting_config["chains"]
intent_config = chains_config["intent"]
chitchat_config = chains_config["chitchat"]
cusine_config = chains_config["cusine"]
intro_config = chains_config["intro"]
need_for_recipe_config = chains_config["need_for_recipe"]
need_for_other_help_config = chains_config["need_for_other_help"]
write_recipe_config = chains_config["write_recipe"]

# Define the LLM for cusine_chain
intent_llm = define_llm(intent_config)
chitchat_llm = define_llm(chitchat_config)
cusine_llm = define_llm(cusine_config)
intro_llm = define_llm(intro_config)
need_for_recipe_llm = define_llm(need_for_recipe_config)
need_for_other_help_llm = define_llm(need_for_other_help_config)
write_recipe_llm = define_llm(write_recipe_config)

# Define intent chain
intent_chain = intent_template | intent_llm

# intent_chain.invoke({"question": "煮乜嘢好?"})

# Define chitchat chain
chitchat_chain = chitchat_template | chitchat_llm

# chitchat_chain.invoke({"question": "煮乜嘢好?"})

# Define cusine chain
cusine_chain = cusine_template | cusine_llm

# cusine_chain.invoke({"question": "煮乜嘢好?", "extra_requirements": []})
# cusine_chain.invoke({"question": "我需要一些煮食想法"})
# cusine_chain.invoke({"question": "hi"})

# Define intro chain
intro_chain = intro_template | intro_llm

# Define need for recipe chain
need_for_recipe_chain = need_for_recipe_template | need_for_recipe_llm

# Define need for other help chain
need_for_other_help_chain = need_for_other_help_template | need_for_other_help_llm

# Define recipe chain
write_recipe_chain = write_recipe_template | write_recipe_llm
