from flask import Flask, render_template
from news import get_news
from ai_analysis import analyze_article
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

analysis_cache = {}

@app.route('/')
def index():
    news_data = get_news(NEWS_API_KEY)
    articles = news_data.get('results', [])

    for article in articles:
        if article.get('content'):
            article_id = article.get('article_id')
            if article_id in analysis_cache:
                article['analysis'] = analysis_cache[article_id]
            else:
                analysis = analyze_article(OPENAI_API_KEY, article['content'])
                analysis_cache[article_id] = analysis
                article['analysis'] = analysis

    return render_template('index.html', articles=articles)

@app.route('/chart')
def chart():
    return render_template('chart.html')

if __name__ == '__main__':
    app.run(debug=True)
