# [NewsSourceHighlights](https://news-sources-highlight.herokuapp.com/)
## News Highlight is a web application meant to dislpay news source and there artciles 
#### By **[Ian Odhiambo](https://github.com/ianodad)**

## Description
The application know has news highlight is a plicatio that uses a newsapi json to display various news source. The news source
are later defined and categories by there very onw news types. The news source will then display link s to eather take the user to the main site or
a way to display more articles in relation to thats source.

Click [here](https://news-sources-highlight.herokuapp.com/) to see the live sit

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On Loading the page** | List of various news sources is displayed per category |
| Display Business | **Clicking on menu categories Business** | Directs to Business sources |
| Display Entertainment | **Clicking on menu categories Entertainment** | Directs to Entertainment sources |
| Display Technology | **Clicking on menu categories Technology** | Directs to Technology Sources |
| Display Science | **Clicking on menu categories Science** | Directs to Science sources |
| Display Articles from a news source | **Clicking the news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On Loading the page**  | Each article displays an image, title, description and publication date |

## Prerequiites
    - Python 3.6 required
	

## Set-up and Installation
    - Clone the Repo
    - Edit the start.sh file with your api key from the news.org website
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6
* gunicorn==19.7.1


## Known bugs
No known errors if found drop a message on my profile

## Technologies used
    - Python 3.6
    - HTML 5
    - Bootstrap 4

## Support and contact details
Contact me on developer Ianodad@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Ian Odhiambo**
