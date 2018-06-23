# -*- coding: utf-8 -*-
import scrapy
from work.items import WorkItem
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider,Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(LinkExtractor(allow=('start=\d+',)), callback = 'parse_item',follow=True),
    )

    def parse_item(self, response):
        works = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for work in works:
        	item = WorkItem()
        	name = work.xpath('./td[1]/a/text()').extract_first()
        	category = work.xpath('./td[2]/text()').extract_first()
        	peoplenum = work.xpath('./td[3]/text()').extract_first()
        	location = work.xpath('./td[4]/text()').extract_first()
        	time = work.xpath('./td[5]/text()').extract_first()
        	item['name'] = name
        	item['category'] = category
        	item['peoplenum'] = peoplenum
        	item['location'] = location
        	item['time'] = time
        	yield item

        
