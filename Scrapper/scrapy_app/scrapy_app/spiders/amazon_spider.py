import scrapy
from scrapy_app.items import IphoneItem 

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.fr']
    start_urls = ['https://www.amazon.fr/s?k=iphone15']

    def parse(self, response):
        # Itère sur chaque produit
        for product in response.css('div.s-result-item'):
            # Extraction du nom et du prix
            name = product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product.css('.a-offscreen::text').get()

            item = IphoneItem()
            item['name'] = name.strip() if name else 'N/A'  # Gère les cas où le nom n'est pas trouvé
            item['price'] = price.strip() if price else 'N/A'  # Gère les cas où le prix n'est pas trouvé
            yield item



