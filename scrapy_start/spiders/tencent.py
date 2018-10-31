# -*- coding: utf-8 -*-
import scrapy
import re
# from scrapy_start.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        items = response.xpath('//*[contains(@class,"odd") or contains(@class,"even")]')
        for item in items:
            # tencent_item = TencentItem()
            temp = dict(
                name=item.xpath("./td[1]/a/text()").extract()[0],
                detailLink="http://hr.tencent.com/" + item.xpath("./td[1]/a/@href").extract()[0],
                positionInfo=item.xpath('./td[2]/text()').extract()[0] if len(
                    item.xpath('./td[2]/text()').extract()) > 0 else None,
                peopleNumber=item.xpath('./td[3]/text()').extract()[0],
                workLocation=item.xpath('./td[4]/text()').extract()[0],
                publishTime=item.xpath('./td[5]/text()').extract()[0]
            )
            # tencent_item = temp
            yield temp

        now_page = int(re.search(r"\d+", response.url).group(0))
        print("*" * 100)
        if now_page < 100:
            url = re.sub(r"\d+", str(now_page + 10), response.url)
            print("this is next page url:", url)
            print("*" * 100)
            yield scrapy.Request(url, callback=self.parse)

