from typing import Any
from publicacion import Publicacion
import requests
from bs4 import BeautifulSoup

class Portalinmobiliario:
    
    def __init__(self, url):
        self.url = url
        self.soup = self.get_page_content()

    def get_publicaciones(self):
        return self.extraer_publicaciones()

    def get_page_content(self):
        response = requests.get(self.url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    
    def extraer_publicaciones(self):
        publicaciones = []
        cards = self.soup.find_all('div', class_='ui-search-map-list ui-search-map-list__item')
        for card in cards:
            pub = Publicacion()
            pub.sitio = "portalinmobiliario"
            pub.id = card.attrs['id']
            pub.url = card.contents[0].contents[0].contents[0].attrs["href"]
            pub.url_imagen = card.contents[0].contents[0].contents[0].contents[0].attrs['data-src']
            pub.ubicacion = card.find_all('div', class_="ui-search-result__content-location")[0].contents[0]
            pub.nombre = card.find_all('h2')[0].contents[0]
            pub.precio = int(card.find_all('span', class_="andes-money-amount__fraction")[0].contents[0].replace(".",""))
            
            print(pub)

            publicaciones.append(pub)

        return publicaciones