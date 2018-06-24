# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url+str(offset),]

    def parse(self, response):
        for each in response.xpath('//div[@class="info"]'):
        	item = DoubanItem()
        	#标题
        	title = each.xpath('.//span[@class="title"][1]/text()').extract_first()
        	#演员
        	bd = each.xpath('.//div[@class="bd"]/p/text()').extract_first().strip()                                                        
        	#评分
        	rating_num = each.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
        	#简介
        	quote = each.xpath('.//p[@class="quote"]/span/text()').extract_first()

        	item['title'] = title
        	item['bd'] = bd
        	item['rating_num'] = rating_num
        	item['quote'] = quote
        	yield item

        if self.offset < 225:
        	self.offset += 25
        	yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


