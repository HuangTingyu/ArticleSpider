# -*- coding: utf-8 -*-
import scrapy

from ArticleSpider.items import JobBoleArticleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114671/']

    def parse(self, response):
        article_item = JobBoleArticleItem()
        title = response.xpath('//*[@id="post-114671"]/div[1]/h1/text()').extract()[0]
        create_date = response.xpath('//*[@id="post-114671"]/div[2]/p/text()').extract()[0].strip().replace("·", "").strip()
        praise_nums = int(response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0])
        content = response.xpath('//*[@id="post-114671"]/div[3]').extract()[0]

        # print(title, create_date, praise_nums, content)
        article_item["title"] = title
        article_item["create_date"] = create_date
        article_item["praise_nums"] = praise_nums
        article_item["content"] = content

        yield article_item
        # pass
