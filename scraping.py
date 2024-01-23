import requests
from bs4 import BeautifulSoup
import hashlib
import time
import json
from sitios import *

def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_publicaciones(soup, sitio):
    if sitio == "portalinmobiliario":
        publicaciones = get_publicaciones_portalinmobiliario(soup)
    elif sitio == "yapo":
        publicaciones = get_publicaciones_yapo(soup)
    else:
        publicaciones = []
    
    return publicaciones

if __name__ == "__main__":
    config = json.load(open("config.json"))
    sitio = "yapo"

    page = get_page_content(config["tracking_urls"][sitio])
    publicaciones = get_publicaciones(page, sitio)
    
    pass