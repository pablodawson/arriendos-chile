import json
from sitios import *

def get_publicaciones_individual(sitio, config):

    url = config["tracking_urls"][sitio]

    if sitio == "portalinmobiliario":
        fuente = Portalinmobiliario(url)
    elif sitio == "yapo":
        fuente = Yapo(url)
    elif sitio == "zoominmobiliario":
        fuente = Zoominmobiliario(url)
    elif sitio == "toctoc":
        fuente = TocToc(url)
    
    publicaciones = fuente.get_publicaciones()
    
    return publicaciones

def get_publicaciones(config):
    publicaciones = []
    for sitio in config["tracking_urls"]:
        print("---- Obteniendo publicaciones de {} -----".format(sitio))
        publicaciones += get_publicaciones_individual(sitio, config)
    
    return publicaciones

if __name__ == "__main__":
    config = json.load(open("config.json"))
    #publicaciones = get_publicaciones(config)

    sitio  = "toctoc"
    publicaciones = get_publicaciones_individual(sitio, config)
