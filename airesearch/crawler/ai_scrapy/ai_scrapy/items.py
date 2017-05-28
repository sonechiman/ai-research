# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AngelListItem(scrapy.Item):
    name = scrapy.Field()
    logo = scrapy.Field()
    angellist = scrapy.Field()
    url = scrapy.Field()
    abstract = scrapy.Field()
    original_description = scrapy.Field()
    place = scrapy.Field()
    categories = scrapy.Field()
    employees = scrapy.Field()
    images = scrapy.Field()
    fundings = scrapy.Field()
    followers = scrapy.Field()
