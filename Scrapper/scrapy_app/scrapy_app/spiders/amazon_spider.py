import scrapy
from scrapy_app.items import IphonePriceItem  # Remplacez par le nom de votre projet

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.fr']
    start_urls = ['https://www.amazon.fr/stores/Apple/Touslesmod%C3%A8les_iPhone/page/1C669056-0312-41F0-966C-FBA3BB8CD016']

    def parse(self, response):
        for price_span in response.css('.Price__whole__mQGs5'):
            price_text = price_span.get()
            # Extraction du prix et nettoyage du texte
            price = price_text.replace('<span class="Price__whole__mQGs5">', '').replace('</span>', '').strip()

            item = IphonePriceItem()
            item['price'] = price
            yield item

