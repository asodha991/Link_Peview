from matplotlib import image
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def get_title(html):
    """Scrape page title."""
    title = None
    # if html.title.string:
    #     title = html.title.string
    if html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    elif html.find("meta", property="twitter:title"):
        title = html.find("meta", property="twitter:title").get('content')
    elif html.find("h1"):
        title = html.find("h1").string
    return title

def get_description(html):
    """Scrape page description."""
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find("meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description

def get_image(html):
    """Scrape share image."""
    image = None
    if html.find("meta", property="image"):
        image = html.find("meta", property="image").get('content')
    elif html.find("meta", property="og:image"):
        image = html.find("meta", property="og:image").get('content')
    elif html.find("meta", property="twitter:image"):
        image = html.find("meta", property="twitter:image").get('content')
    elif html.find("img", src=True):
        image = html.find_all("img").get('src')
    return image

def get_url(html):
    """ Get the URL in interface"""
    url = None
    if html.find("meta", property="og:url"):
        url = html.find("meta", property="og:url").get('content')
    elif html.find("meta", property="twitter:url"):
        url = html.find("meta", property="twitter:url").get('content')
    elif html.find("meta", property="url"):
        url = html.find("meta", property="url").get('content')
    return url

def generate_preview(url):
    req = requests.get(url)
    html = BeautifulSoup(req.content, 'html.parser')
    title = get_title(html)
    image = get_image(html)
    description = get_description(html)
    urls = get_url(html)
    
    meta_data = {
       'title': title,
       'description': description,
       'image': image,
    }
    
    # print(meta_data)
    return description, image, title, urls

# generate_preview(url)