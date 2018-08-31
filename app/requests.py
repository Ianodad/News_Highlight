# from main import main
import urllib.request
import json
from .models import News

# getting api key
api_key = '7c1c3351a80d4bb78f19854119971356'

# getting the movie base url
base_url = 'https://newsapi.org/v2/sources?apiKey={}'


def get_news():
    get_news_url = base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)

        news_results = None

        if news_response['sources']:
            news_result_list = news_response['sources']
            news_results = process_results(news_result_list)

    print(news_results)

    return news_results


def process_results(news_list):
    '''
    getting instance of the list
    '''
    news_result = []
    for news in news_list:
        id = news.get('id')
        name = news.get('name')
        descript = news.get('description')
        url = news.get('url')
        cat = news.get('category')
        # date = news.get('date')

        news_object = News(id, name, descript, url, cat)
        news_result.append(news_object)
    return news_result
