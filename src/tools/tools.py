import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import List
from langchain.tools import tool
from langchain_google_community import GoogleSearchAPIWrapper


load_dotenv(override=True)

search = GoogleSearchAPIWrapper()


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
