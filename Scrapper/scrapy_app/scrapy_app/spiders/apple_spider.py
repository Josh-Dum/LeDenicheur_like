# spider pour scrapper apple

import scrapy
from scrapy_app.items import IphonePriceItem

class AppleSpider(scrapy.Spider):
    name = 'apple_spider'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.apple.com/fr/shop/buy-iphone/iphone-15-pro/%C3%A9cran-de-6,1-pouces-128go-titane-naturel']  
    def parse(self, response):
        item = IphonePriceItem()
        item['price'] = response.css('#\37 3bc8841-bde5-11ee-b555-052252469efc_label > span > span.column.form-selector-right-col.rf-bfe-selector-right-col > span > span').get()
        
        yield item