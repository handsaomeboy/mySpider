# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class PracticeSpider(scrapy.Spider):
    name = 'practice'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        res_list = response.xpath('//div[@class="li_txt"]')
        arr = []
        for i in res_list:
            item = MyspiderItem()
            name = i.xpath('./h3/text()').extract()[0]
            title = i.xpath('./h4/text()').extract()[0]
            info = i.xpath('./p/text()').extract()[0]
            #print name
            item['name'] = name.encode('gbk')
            item['title'] = title.encode('gbk')
            item['info'] = info.encode('gbk')
            arr.append(item)
        return arr
