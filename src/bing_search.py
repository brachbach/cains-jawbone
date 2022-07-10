from os import environ
import requests
from dataclasses import dataclass

BING_API_URL = "https://api.bing.microsoft.com/v7.0/search"

@dataclass
class BingSearchResult:
    snippet: str
    url: str

def search_bing(query: str) -> dict:
    headers = {"Ocp-Apim-Subscription-Key": environ['BING_SUBSCRIPTION_KEY']}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(BING_API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_bing_search_results(query: str) -> list[BingSearchResult]:
    response = search_bing(query)
    return [BingSearchResult(snippet=result["snippet"], url=result["url"]) for result in response["webPages"]["value"]]

if __name__ == "__main__":
    print(get_bing_search_results("NOT Cain's NOT Jawbone And I really think I would have preferred the Maestro Jimson’s title, now that this piled abomination is actually before me."))

