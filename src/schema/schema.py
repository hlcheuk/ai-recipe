from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field


class IntentSchema(BaseModel):
    about_cusine: bool = Field(
        description="如用戶在詢問有關菜式的問題，請回傳True; 否則請回傳False"
    )
    extra_requirements: List[str] = Field(
        description="用戶所要求的菜式、煮食的額外要求"
    )


class CusineSchema(BaseModel):
    cusine: List[str] = Field(description="5個菜式名稱", min_items=3, max_items=3)


class GetAvailableIngredientsInput(BaseModel):
    market_location: str = Field(description="the location of the market")
