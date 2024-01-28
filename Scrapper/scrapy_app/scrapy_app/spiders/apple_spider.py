# spider pour scrapper apple

import scrapy
import json
from scrapy_app.items import IphonePriceItem

class AppleSpider(scrapy.Spider):

    name = 'apple_spider'
    allowed_domains = ['apple.com']
    # start_urls = ['https://www.apple.com/fr/shop/buy-iphone/iphone-15-pro/%C3%A9cran-de-6,1-pouces-128go-titane-naturel'] 
    # Utilisation de l'URL XHR
    start_urls = ['https://www.apple.com/fr/shop/updateSEO?m=%7B%22product%22%3A%22MTUX3ZD%2FA%22%2C%22refererUrl%22%3A%22https%3A%2F%2Fwww.apple.com%2Ffr%2Fshop%2Fbuy-iphone%2Fiphone-15-pro%2F%25C3%25A9cran-de-6%2C1-pouces-128go-titane-naturel%22%7D'] 
    
    def parse(self, response):
        # Conversion de la réponse en JSON
        data = json.loads(response.text)
        price_info = data.get('body', {}).get('marketingData', {}).get('offers', [{}])[0]

        item = IphonePriceItem()
        # Extraction du prix
        item['price'] = price_info.get('price', 'Non trouvé')
        
        yield item