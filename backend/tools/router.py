def decide_tool(query):
    query = query.lower()

    web_keywords = ["latest", "news", "today", "recent", "current"]

    for word in web_keywords:
        if word in query:
            return "web_search"

    return "rag"