# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovernmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GovernmentItem(scrapy.Item):
    title = scrapy.Field()
    ConstructDept0 = scrapy.Field()
    directSpecialDept1 = scrapy.Field()
    directDept2 = scrapy.Field()
    ManageDept3 = scrapy.Field()
    otherDept4 = scrapy.Field()
    directInstitution5 = scrapy.Field()
    InstitutionOfManageDept6 = scrapy.Field()