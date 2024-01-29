import scrapy
from scrapy_app.items import IphoneItem 

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.fr']
    start_urls = ['https://www.amazon.fr/s?k=iphone15']

    def parse(self, response):
        for product in response.css('div[data-asin]'):
            name = product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product.css('.a-offscreen::text').get()

            if name and price:
                yield {
                    'name': name.strip(),
                    'price': price.strip()
                }
            else:
                self.logger.info(f"Produit manquant : {product.attrib['data-asin']}")



