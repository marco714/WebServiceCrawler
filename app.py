from fastapi import FastAPI
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl

import requests

app = FastAPI()


class URL(BaseModel):
    url:HttpUrl


def get_title(soup):
    return soup.head.find('title').text if soup.head.find('title') else None

def get_description(soup):
    main_description = soup.head.find('meta', attrs={'name':'description'}).get('content') if soup.head.find('meta', attrs={'name':'description'}) else None


    og_description = soup.find('meta', property="og:description").get('content') if soup.find('meta', property="og:description") else None

    return main_description or og_description or None

def get_keywords(soup):

    keywords = soup.head.find('meta', attrs={'name':'keywords'}).get('content') if soup.head.find('meta', attrs={'name':'keywords'}) else None

    return keywords

def get_image(soup):

    return soup.find('meta', property="og:image").get('content') if soup.find('meta', property="og:image") else None

@app.get('/')
def index():

    return {'message':"Hello World"}

@app.get('/about')
def about():

    return {'about':"Version 2"}

@app.post('/scrap_tags')
async def scrape_tags(url: URL):

    page = requests.get(str(url.url))


    soup = BeautifulSoup(page.text, 'html.parser')
    
    
    # import pdb
    # pdb.set_trace()

    return {
        "title":get_title(soup),
        "description":get_description(soup),
        "Keywords":get_keywords(soup),
        "Image":get_image(soup)
    }


