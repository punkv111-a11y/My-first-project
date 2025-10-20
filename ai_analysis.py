from openai import OpenAI

def analyze_article(api_key, article_content):
    try:
        client = OpenAI(api_key=api_key)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that analyzes news articles. "
                    "Provide a one-sentence summary and a sentiment score (positive, negative, or neutral)."
                ),
            },
            {
                "role": "user",
                "content": f"Analyze the following news article:\n\n{article_content}",
            },
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error analyzing article: {e}")
        return "Error: Unable to analyze article."
