from typing import Any
from publicacion import Publicacion
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#ElementNotVisibleException
from selenium.common.exceptions import ElementNotVisibleException

import requests
from bs4 import BeautifulSoup
import time

from utils import extraer_info_descripcion

import os

class Yapo:
    
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.webdriver = webdriver.Chrome(options=options)
        self.url = url
        self.soup = self.get_page_content()
        self.inferir_ubicacion = True

    def get_publicaciones(self):
        return self.extraer_publicaciones()

    def get_page_content_unloaded(self, url=""):
        if url == "":
            url = self.url
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def get_page_content(self, url=""):
        if url == "":
            url = self.url
        
        self.webdriver.get(url)

        time.sleep(2)
        soup = BeautifulSoup(self.webdriver.page_source, 'html.parser')
        return soup

    def extraer_publicaciones(self):
        publicaciones = []
        cards = self.soup.select("body > app-root > listing-index > listing-main > div.ng-tns-c2811353138-0.align-items-stretch.container.d-flex.gap-5.justify-content-start.main-listing.pb-4.pt-4.pt-lg-6.inmo > div.col-right.w-100 > listing-result-list > listing-result-list-content")[0].contents

        for card in cards:
            if card == " ":
                continue

            pub = Publicacion()
            pub.sitio = "yapo"
            try:
                pub.nombre = card.contents[0].contents[1].contents[0].find('h2').contents[0]
                pub.url = "https://www.yapo.cl" + card.contents[0].attrs['href']
                pub.url_imagen = card.find_all("img")[1].attrs['src']
                pub.descripcion = card.contents[0].contents[1].contents[1].contents[0].contents[2].contents[0]
                pub.precio =  int(card.contents[0].contents[1].contents[1].contents[0].contents[1].contents[2].contents[1].replace(".","").replace("$","").strip())
                pub.dormitorios = int(card.contents[0].contents[1].contents[1].contents[1].select(".value")[0].contents[0])
                if (self.inferir_ubicacion):
                    pub.ubicacion = extraer_info_descripcion(pub.descripcion)
                
                print(pub)

                publicaciones.append(pub)
            except:
                continue

        return publicaciones
    
    