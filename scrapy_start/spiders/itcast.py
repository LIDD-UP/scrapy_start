# -*- coding: utf-8 -*-
import scrapy
from scrapy_start.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # with open('teacher.html','w',encoding='utf-8') as f:
        #     f.write(response.text)
        #     print(response.text)
        items = []
        # 找到所有的老师根节点：
        for teacher in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem
            name = teacher.xpath("h3/text()").extract()[0].encode('utf-8').decode('unicode-escape')
            level = teacher.xpath("h4/text()").extract()
            info = teacher.xpath('p/text()').extract()
            item = ItcastItem()
            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]

            items.append(item)
        return items
        # yield items
