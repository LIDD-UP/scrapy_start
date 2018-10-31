# -*- coding: utf-8 -*-
import scrapy
from scrapy_start.items import DoubanItem
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=25&filter=']

    def parse(self, response):
        movies = response.xpath("//div[@class='info']")
        for movie in movies:
            doubanItem =DoubanItem()
            title = movie.xpath("div[@class='hd']/a/span[@class='title']/text()").extract()[0]
            content = movie.xpath("div[@class='bd']/p/text()").extract()[0]
            star = movie.xpath("div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            info = movie.xpath("div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract()[0]
            doubanItem['title'] = title
            doubanItem['content'] = content
            doubanItem['star'] = star
            doubanItem['info'] = info
            yield doubanItem
        print(response.url)
        now_page = re.findall(r'start=(\d+)&filter',response.url)

        print(now_page)
        now_page = int(now_page[0])
        if now_page <100:
            next_url ='https://movie.douban.com/top250?start={}&filter='.format(now_page+25)
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse)

