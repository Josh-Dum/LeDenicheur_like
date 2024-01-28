# spider pour scrapper apple

import scrapy
import json
from scrapy_app.items import IphonePriceItem
import json

class AppleSpider(scrapy.Spider):

    name = 'apple_spider'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.apple.com/fr/shop/updateSEO?m=%7B"product"%3A"MTUX3ZD%2FA"%2C"refererUrl"%3A"https%3A%2F%2Fwww.apple.com%2Ffr%2Fshop%2Fbuy-iphone%2Fiphone-15-pro%2F%C3%A9cran-de-6%2C1-pouces-128go-titane-naturel"%7D']

    def parse(self, response):

        # Charger la réponse JSON
        data = json.loads(response.text)
        # Extraire le prix à partir du chemin JSON
        item = IphonePriceItem()

        # Accéder à l'information sur le prix
        price_info = data['body']['marketingData']['microdataList'][0]
        microdata = json.loads(price_info)
        
        if '@type' in microdata and microdata['@type'] == 'Product':

            price = microdata['offers'][0]['price']

            item['price'] = price

            yield item