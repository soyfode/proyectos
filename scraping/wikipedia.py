from scrapy.item import Field
from scrapy.item import Item
from scrapy.item import Spider
from scrapy.item import Selector
from scrapy.item import ItemLoader

encabezados = {
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

idiomas = parser.find_class('central-featured-lang')

for idioma in idiomas:
    print(idioma.text_content())
