import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import List
from langchain.tools import tool
from langchain_google_community import GoogleSearchAPIWrapper


load_dotenv(override=True)

search = GoogleSearchAPIWrapper()

# class GetAvailableIngredientsInput(BaseModel):
# market_location: str = Field(default=None, description="街市位置")
# attributes: List[str] = Field(default=None, description="有關煮食想法的要求")


# @tool(args_schema=GetAvailableIngredientsInput)
def get_available_ingredients(market_location: str = None):
    "當用家詢問有關煮食的想法時，你必須調用此工具來尋找可供使用的食材."
    ingredients = """<pork>
    美國排骨粒 454克
    泰國冰鮮豬肋排骨 280g
    優質冰鮮豬展(三無豬) 1盒 約280克
    梅肉切片 200克
    優質冰鮮瘦肉(三無豬) 1盒 約320克
    </pork>

    <beef>
    優質秘製調味滑牛 1盒 約300克
    加拿大 穀飼頂級AAA肥牛火鍋 300克
    安格斯冰鮮肉眼牛扒 180克
    優質冰鮮牛肉 1盒 約300克
    美國優質牛肋條 454g
    </beef>

    <chicken>
    雞柳 681克 (急凍)
    雞上髀去皮無骨 330克
    雞下髀 345克
    雞中翼 280克
    雞胸肉去皮 400克
    </chicken>

    <seafood>
    挪威三文魚柳 (帶皮) 500克
    格靈蘭比目魚扒 (手釣魚) 400克
    大西洋鱈魚柳 250克
    野生海捕麻蝦肉 200克
    急凍熟帆立貝 1包 約1000克
    </seafood>
    """
    return ingredients


@tool
def google_search_scrape(query: str):
    "Search Google for recent results."
    # Define domain to exclude
    exclude_domain = ["youtube", "wikipedia", "madewithlau", "cookpad"]
    pattern = "|".join(re.escape(domain) for domain in exclude_domain)
    # Peform search
    search_results = search.results(query, len(exclude_domain) + 2)
    # Apply domain filter
    search_results = [
        search_result
        for search_result in search_results
        if bool(re.search(pattern, search_result["link"])) == False
    ]
    search_results = [search_results[0]]
    links = [search_result["link"] for search_result in search_results]
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.find("body")
        if body:
            body_text = body.get_text()
            return {"body_text": body_text, "link": link}
