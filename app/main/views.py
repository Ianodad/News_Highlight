from flask import render_template
from . import main  # importing data from main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles


@main.route('/')
def index():
    general = get_sources('general')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    science = get_sources('science')

    # for i in real_news:
    #     print(i.name)
    title = "hello world"
    return render_template('index.html', title=title, general=general, business=business, entertainment=entertainment, technology=technology, science=science)

@main.route('/articles/<int:id>')
def article(id):
    '''
    view all article based of each source
    '''

    article = 