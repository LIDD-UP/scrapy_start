# -*- coding: utf-8 -*-
import json
from scrapy_start import settings
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyStartPipeline(object):
    def process_item(self, item, spider):
        return item


class ItemJsonPipeline(object):
    def __init__(self):
        self.file = open('teacher.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False) +'\n'
        self.file.write(content)
        return item
    def close_spider(self,spider):
        self.file.close()


class TencentJsonPipeline(object):

    def __init__(self):
        #self.file = open('teacher.json', 'wb')
        self.file = open('tencent.json', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()


from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host,port=port)

        # 指向指定的数据库
        mdb = client[dbname]
        # 获取数据库里存放数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        data = dict(item)
        # 向指定的表里添加数据
        self.post.insert(data)
        return item
