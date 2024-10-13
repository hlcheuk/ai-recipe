import operator
from typing import Annotated, Sequence, TypedDict, List
from langchain_core.messages import BaseMessage


class OverallState(TypedDict):
    question: str
    about_cusine: bool
    recipe_need: str
    extra_requirements: List[str]
    cusine_choices: List[str]
    cusine_intro: Annotated[List[dict], operator.add]
    cusine_recipe_link: Annotated[List[dict], operator.add]
    messages: Annotated[Sequence[BaseMessage], operator.add]
    last_node: str


class CusineState(TypedDict):
    cusine: str
    intro: str


class PickIngredientsState(TypedDict):
    cusine: str
    intro: str
