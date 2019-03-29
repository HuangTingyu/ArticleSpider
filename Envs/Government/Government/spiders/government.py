# -*- coding: utf-8 -*-
import scrapy

from Government.items import GovernmentItem

class GovernmentSpider(scrapy.Spider):
    name = 'government'
    allowed_domains = ['http://www.gd.gov.cn/govpub/jg']
    start_urls = ['http://www.gd.gov.cn/govpub/jg']

    def parse(self, response):
        government_item = GovernmentItem()
        title = response.xpath('//*[@class="tit1"]/a/text()').extract()
        ConstructDept0 = response.xpath('/html/body/div[3]/div[2]/div/div/ul/li/a/text()').extract()
        directSpecialDept1 = response.xpath('/html/body/div[3]/div[3]/div/ul/li/a/text()').extract()
        directDept2 = response.xpath('/html/body/div[3]/div[4]/div/ul/li/a/text()').extract()
        ManageDept3 = response.xpath('/html/body/div[3]/div[5]/div/ul/li/a/text()').extract()
        otherDept41 = response.xpath('/html/body/div[3]/div[6]/div/ul[1]/li/a/text()').extract()
        otherDept42 = response.xpath('/html/body/div[3]/div[6]/div/ul[1]/li/text()').extract()
        otherDept43 = response.xpath('/html/body/div[3]/div[6]/div/ul[2]/li/a/text()').extract()
        directInstitution5 = response.xpath('/html/body/div[3]/div[7]/div/ul/li/a/text()').extract()
        InstitutionOfManageDept6 = response.xpath('/html/body/div[3]/div[8]/div/ul/li/a/text()').extract()
        # print(title, ConstructDept0, directSpecialDept1, directDept2, ManageDept3)
        # print(otherDept41, otherDept42, otherDept43)
        otherDept4 = otherDept41 + otherDept42 + otherDept43
        # print(otherDept4)
        # print(directInstitution5, InstitutionOfManageDept6)
        government_item["title"] = title
        government_item["ConstructDept0"] = ConstructDept0
        government_item["directSpecialDept1"] = directSpecialDept1
        government_item["directDept2"] = directDept2
        government_item["ManageDept3"] = ManageDept3
        government_item["otherDept4"] = otherDept4
        government_item["directInstitution5"] = directInstitution5
        government_item["InstitutionOfManageDept6"] = InstitutionOfManageDept6

        yield government_item
