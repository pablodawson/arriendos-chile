from publicacion import Publicacion
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse, parse_qs

class Zoominmobiliario:
    
    def __init__(self, url):
        self.url = url
        self.soup = self.get_page_content_unloaded()

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
        cards = self.soup.select(".card-property")

        for card in cards:
            url = card.find_all('a')[-1].attrs['href']
            try:
                pub = Publicacion()
                pub.sitio = "zoominmobiliario"
                pub.url = url
                pub.nombre = card.find(class_="truncate nameProperty").contents[0].strip()
                pub.url_imagen = card.find_all('img')[0].attrs['data-src']
                pub.dormitorios = int(card.find(class_="list-inline list-inline-characteristics").contents[3].select('.space')[0].contents[0].strip())
                pub.precio = int(card.select(".price-value")[0].contents[0].replace(".",""))
                pub.ubicacion = card.find(class_="truncate address").contents[0].strip()

                soup_pub = self.get_page_content_unloaded(pub.url)
                
                coords_url = self.get_page_content_unloaded(pub.url).find(class_="btn zm-btn btn-zoom").attrs['href']
                parsed_url = urlparse(coords_url)
                query_parameters = parse_qs(parsed_url.query)

                latitud = float(query_parameters['lat'][0])
                longitud = float(query_parameters['lng'][0])

                pub.coordenadas = [latitud, longitud]
                print(pub)
                
                publicaciones.append(pub)

            except:
                continue
        
        return publicaciones