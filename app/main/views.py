from flask import render_template
from . import main  # importing data from main
from ..requests import get_news
from ..models import News


@main.route('/')
def index():
    general = get_news('general')
    business = get_news('business')
    entertainment = get_news('entertainment')
    technology = get_news('technology')
    science = get_news('science')

    # for i in real_news:
    #     print(i.name)
    title = "hello world"
    return render_template('index.html', title=title, general=general, business=business, entertainment=entertainment, technology=technology, science=science)
