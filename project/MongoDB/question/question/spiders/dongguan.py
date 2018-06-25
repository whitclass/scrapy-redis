# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from question.items import QuestionItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+')),
        Rule(LinkExtractor(allow=r'/2018\d+/\d+.shtml'), callback='parse_item',follow=True),
    )

    def parse_item(self, response):
    	item = QuestionItem()
    	title = response.xpath("//div[@class='pagecenter p3']//div[@class='cleft']/strong/text()").extract_first()
    	content = response.xpath("//div[@class='c1 text14_2']/text()").extract_first()
    	item['title'] = title.replace(' ','')
    	item['content'] = content.replace(' ','')
    	yield item
        
        
