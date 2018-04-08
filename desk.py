# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bizhi.items import BizhiItem

class DeskSpider(CrawlSpider):
    name = 'desk'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/5118_63375_2.html']

    rules = (
        Rule(LinkExtractor(allow=r'bizhi/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        im_head = response.xpath('.//div[@class="wrapper photo-tit clearfix"]')
        im_url = response.xpath('.//div[@class="photo"]/div')
        for each,u in zip(im_head,im_url):
            item = BizhiItem()
            item['name'] = each.xpath('./h3/a/text()').extract()[0]
            item['num'] = each.xpath("./h3/span/span/text()").extract()[0]
            item['image_url'] = u.xpath("./img/@src").extract()
            # print(item['name'])
            # print(item['num'])
            # print(item['image_url'])
            yield item

