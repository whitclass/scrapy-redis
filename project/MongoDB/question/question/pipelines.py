# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class QuestionPipeline(object):
	def __init__(self):
		#获取设置里的MONGODB主机，端口，数据库和表名称
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbname = settings['MONGODB_DBNAME']
		tbname = settings['MONGODB_TBNAME']

		#pymongo.MongoClient(host, port) 创建MongoDB链接
		client = pymongo.MongoClient(host=host,port=port)

		#指向指定的数据库
		mydb = client[dbname]

		#数据表
		self.mytb = mydb[tbname]
	
	def process_item(self, item, spider):
		data = dict(item)
		self.mytb.insert(data)  
		return item
