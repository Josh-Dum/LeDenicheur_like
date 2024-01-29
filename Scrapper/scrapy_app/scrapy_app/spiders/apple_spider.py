# spider pour scrapper apple

import scrapy
from scrapy_splash import SplashRequest

class AppleSpider(scrapy.Spider):
    name = 'apple_spider'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.e.leclerc/fp/smartphone-apple-iphone-15-pro-max-256gb-noir-titanium-0195949048258']

    def start_requests(self):
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, 
                                args={'wait': 3, 'user_agent': user_agent})


    def parse(self, response):
        # Affichage du code HTML renvoyé par Splash
        self.logger.info("HTML Body: %s", response.text)

