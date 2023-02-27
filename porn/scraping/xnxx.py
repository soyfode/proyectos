from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Xnxx(Item):
    nombre = Field()
    numero = Field()

class xnxxSpider(CrawCrawllSpider):
    name = "xnxx"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        #'FEED_EXPORT_FIELDS': ["titulo","fecha","hora"],
        #'CLOSESPIDER_PAGECOUNT': 20,
        #'CLOSESPIDER_ITEMCOUNT': 20,
        #'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes
    }

    download_delay = 1

    allowed_domains = ['xnxx.com/tags']

    start_urls = ['https://www.xnxx.com/tags']

    rules = (
        Rule(
        LinkExtractor(
            allow=r'/a'
            ),follow=True, callback='parse_items'
        ),
    )
    

    def parse_items(self, response):
        item = ItemLoader(Xnxx(), response)

        item.add_xpath('nombre', '//*[@id="tags"]/li/a/text()')
        item.add_xpath('numero', '//*[@id="tags"]/li/strong/text()')

        yield item.load_item()

