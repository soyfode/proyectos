from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class celebridad(Item):
    nombre = Field()
    precio = Field()
    tipo = Field()

class famososSpider(Spider):
    name = 'famosos'
    custom_setting={ "USER_AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" }

    start_urls = ['https://www.famosos.com/buscar?country_id=25%2C30%2C31&category_id=5%2C4%2C3&limit=20']

    def parse(self, response):
        sel = Selector(response)
        artistas = sel.xpath('//div[@class="celebrity-details"]')
        for artista in artistas:
            item = ItemLoader(Artista(),artista)
            item.add_xpath('nombre','.//h3/text()')
            yield  item.load_item()


