from typing import Any
from publicacion import Publicacion
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
import time

from utils import extraer_info_descripcion

import os

class TocToc:
    
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        self.webdriver = webdriver.Chrome(options=options)
        self.url = url
        self.soup = self.get_page_content()

    def get_publicaciones(self):
        return self.extraer_publicaciones()

    def get_page_content_unloaded(self, url=""):
        if url == "":
            url = self.url
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def get_page_content(self, url="", wait_for_element="#sva-i-li-card-propiedades"):
        if url == "":
            url = self.url
        self.webdriver.get(url)
        WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, wait_for_element)))
        content = self.webdriver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    
    def extraer_publicaciones(self):
        publicaciones = []
        
        cards = self.soup.find_all(id="sva-i-li-card-propiedades")
        
        for card in cards:
            pub = Publicacion()
            pub.sitio = "toctoc"
            
            try:
                info = card.attrs
                pub.id = info['data-id-propiedad']
                pub.nombre = info['data-lista']
                pub.precio =  int(info['data-precio1'])
                pub.dormitorios = int(info['data-dormitorios1'])
                pub.ubicacion = info['data-comuna']
                pub.url = card.find('a').attrs['href']
                pub.url_imagen = card.find('picture').contents[0].attrs['srcset']

                soup_publicacion = self.get_page_content(pub.url, ".btn-outline")

                pub.descripcion = soup_publicacion.find(class_="bl c-informacion-adicional").find_all('p')[1].contents[0]
                ubicacion_url = soup_publicacion.find(class_="btn-outline").attrs['href']
                parsed_url = urlparse(ubicacion_url)
                coords = parse_qs(parsed_url.query)['q'][0].split(',')

                pub.coordenadas = [float(coords[0]), float(coords[1])]
                
                print(pub)

                publicaciones.append(pub)
            
            except:
                continue

        return publicaciones
    
    