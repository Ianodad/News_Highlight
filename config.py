class Config:

    NEWHIGHLIGHT_API_URL = 'https://newsapi.org/v2/sources?apiKey={}'


class ProdConfig(Config):


class DevConfig(Config):

    DEBUG = True
