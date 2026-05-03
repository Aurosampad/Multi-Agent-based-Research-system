from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from functools import lru_cache

# ✅ Explicitly load .env from project root
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))


# ✅ Lazy + cached Tavily client (VERY IMPORTANT)
@lru_cache(maxsize=1)
def get_tavily_client():
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError(
            "❌ TAVILY_API_KEY not found. Check your .env file or environment variables."
        )

    return TavilyClient(api_key=api_key)


# 🔍 Web Search Tool
@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and snippets."""

    try:
        tavily = get_tavily_client()
        results = tavily.search(query=query, max_results=5)

        out = []
        for r in results.get("results", []):
            out.append(
                f"Title: {r.get('title','N/A')}\n"
                f"URL: {r.get('url','N/A')}\n"
                f"Snippet: {r.get('content','')[:300]}\n"
            )

        return "\n----\n".join(out) if out else "No results found."

    except Exception as e:
        return f"❌ Web search failed: {str(e)}"


# 🌐 Scraper Tool
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""

    try:
        resp = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        if resp.status_code != 200:
            return f"❌ Failed to fetch page. Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove noisy tags
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:3000] if text else "No readable content found."

    except Exception as e:
        return f"❌ Could not scrape URL: {str(e)}"
