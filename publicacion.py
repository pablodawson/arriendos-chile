import time

class Publicacion:
    def __init__(self,
                 id=0,
                 sitio = "",
                 nombre="", 
                 descripcion="",
                 url="",
                 url_imagen="",
                 fecha=time.strftime("%d/%m/%y"),
                ubicacion="",
                 precio=0,
                 dormitorios=0,
                 coordenadas=[]):

        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.url = url
        self.url_imagen = url_imagen
        self.fecha = fecha
        self.precio = precio
        self.ubicacion = ubicacion
        self.coordenadas = coordenadas
        self.sitio = sitio
        self.dormitorios = dormitorios

    def __str__(self):
        return self.nombre