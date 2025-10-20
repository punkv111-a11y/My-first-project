from newsdataapi import NewsDataApiClient

def get_news(api_key):
    try:
        api = NewsDataApiClient(apikey=api_key)
        response = api.news_api(q="indian stocks", country="in")
        return response
    except Exception as e:
        print(f"Error fetching news: {e}")
        return {}
