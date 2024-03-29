# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class IphoneItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()
    stockage = scrapy.Field()
    gamme = scrapy.Field()
    couleur = scrapy.Field()
    datetime = scrapy.Field()
    link = scrapy.Field()