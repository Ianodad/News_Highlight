import os

# Getting the url key
api_key = None

# Getting base url
news_article_base_url = None
news_source_base_url = None
news_highlight_base_url =None
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apikey={}'
    NEWS_TOPHEADLINES_BASE_URL = ''

    NEWS_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
