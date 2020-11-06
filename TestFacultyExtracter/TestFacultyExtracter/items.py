# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestfacultyextracterItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    imageUrl=scrapy.Field()
    url=scrapy.Field()

class TestfacultyextracterItem2(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    name=scrapy.Field()
    url=scrapy.Field()