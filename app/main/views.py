from flask import render_template
from . import main  # importing data from main
from ..requests import get_news
from ..models import News


@main.route('/')
def index():
    real_news = get_news()
    print(real_news)
    title = "hello world"
    return render_template('index.html', title=title, news=real_news)
