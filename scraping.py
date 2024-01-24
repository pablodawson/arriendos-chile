import json
from sitios import *

def get_publicaciones(sitio, config):

    url = config["tracking_urls"][sitio]

    if sitio == "portalinmobiliario":
        fuente = Portalinmobiliario(url)
    elif sitio == "yapo":
        fuente = Yapo(url)
    
    publicaciones = fuente.get_publicaciones()
    
    return publicaciones

if __name__ == "__main__":
    config = json.load(open("config.json"))
    sitio = "yapo"
    
    publicaciones = get_publicaciones(sitio, config)