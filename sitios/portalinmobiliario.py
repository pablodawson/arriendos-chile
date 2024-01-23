from publicacion import Publicacion

def get_publicaciones(soup):

    publicaciones = []

    cards = soup.find_all('div', class_='ui-search-map-list ui-search-map-list__item')

    for card in cards:
        pub = Publicacion()
        pub.sitio = "portalinmobiliario"
        pub.id = card.attrs['id']
        pub.url = card.contents[0].contents[0].contents[0].attrs["href"]
        pub.url_imagen = card.contents[0].contents[0].contents[0].contents[0].attrs['data-src']
        pub.ubicacion = card.find_all('div', class_="ui-search-result__content-location")[0].contents[0]
        pub.nombre = card.find_all('h2')[0].contents[0]
        pub.precio = int(card.find_all('span', class_="andes-money-amount__fraction")[0].contents[0].replace(".",""))
        publicaciones.append(pub)

    return publicaciones