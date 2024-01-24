from publicacion import Publicacion

class Template:
    
    def __init__(self, url):
        self.url = url
        self.content = self.get_page_content()

    def get_publicaciones(self):
        return self.extraer_publicaciones()

    def get_page_content(self):
        content = None
        return content
    
    def extraer_publicaciones(self):
        publicaciones = []
        cards = None
        return publicaciones