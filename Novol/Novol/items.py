# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Books(scrapy.Item):
    title=scrapy.Field()
    yxhj = scrapy.Field()
    xsyy = scrapy.Field()
    xslx = scrapy.Field()
    xszz = scrapy.Field()
    xsdx = scrapy.Field()
    gxsj = scrapy.Field()
    download_url=scrapy.Field()