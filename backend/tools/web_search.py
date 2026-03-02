import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):
    try:
        response = client.search(
            query=query,
            search_depth="basic",
            max_results=3
        )

        results = []

        for r in response["results"]:
            results.append(f"{r['title']}\n{r['content']}")
        print("From Web Search")
        return "\n\nFrom Web Search".join(results)

    except Exception as e:
        return f"Web search error: {str(e)}"