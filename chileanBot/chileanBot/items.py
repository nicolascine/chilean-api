# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ChileanbotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    photo = scrapy.Field()
    circumscription = scrapy.Field()
    email = scrapy.Field()
    phone =scrapy.Field()
    pass
