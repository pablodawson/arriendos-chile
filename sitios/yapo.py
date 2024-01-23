from publicacion import Publicacion

def get_publicaciones(soup):
    
    publicaciones = []

    # Find cards, they are of type listing-result-ad
    cards = soup.select("body > app-root > listing-index > listing-main > div.ng-tns-c2811353138-0.align-items-stretch.container.d-flex.gap-5.justify-content-start.main-listing.pb-4.pt-4.pt-lg-6.inmo > div.col-right.w-100 > listing-result-list > listing-result-list-content")[0].contents

    for card in cards:
        pub = Publicacion()
        pub.sitio = "yapo"
        pub.id = 0
        pub.url = card.contents[0].contents[0].attrs["href"]
        pub.url_imagen = card.select("listing-result-ad:nth-child(1) > a > div.cover-container.ratio.ratio-1x1 > div.img-inner.ng-star-inserted > img")[0]
        pub.ubicacion = card.find_all('div', class_="listing__item--location")[0].contents[0]
        pub.nombre = card.find_all('div', class_="listing__item--title")[0].contents[0]
        pub.precio = int(card.find_all('div', class_="listing__item--price")[0].contents[0].replace(".",""))
        publicaciones.append(pub)
    pass