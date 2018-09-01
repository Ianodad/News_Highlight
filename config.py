class Config:

    NEWHIGHLIGHT_API_URL = 'https://newsapi.org/v2/sources?apiKey={}'


class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass


class DevConfig(Config):

    DEBUG = True
