# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
import time

class RengongzhinengSpider(scrapy.Spider):
    name = 'rengongzhineng'
    allowed_domains = ['www.leiphone.com']
    #start_urls = ['http://www.leiphone.com/']
    start_urls = ['https://www.leiphone.com/category/ai']

    def decorate(fun):
        '''
        打印函数被调用的时间及调用次数
        '''
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            start_time = time.time()
            data = fun(*args, **kwargs)
            stop_time = time.time()
            dt = stop_time - start_time
            count += 1
            print("被调用%d次，本次调用花费时间%f秒。" % (count, dt))
            return data

        return wrapper

    def parse(self, response):
        '''
        1. 获取文章列表页中的url并交给解析函数进行具体字段的解析
        2. 获取下一页的url并交给scarpy进行下载，下载完成后交给parse
        '''

        # 获取文章列表页中的url并交给解析函数进行具体字段的解析

        post_urls = response.css(".word h3 a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail)

        #提取下一页并交给scrapy进行下载
        next_url = response.css(".next::attr(href)").extract()[1]
        next_url = parse.urljoin(response.url,next_url)
        if next_url:
            yield Request(url=next_url, callback=self.parse)

    @decorate
    def parse_detail(self,response):
        #提取文章的具体字段

        title = response.xpath("/html/body/div[6]/div[1]/div[1]/div/h1/text()").extract()[0].strip()
        print(title)
        content = response.xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div[1]").extract()[0]
        create_data = response.xpath("//td[@class='time']/text()").extract()[0].strip()
        author = response.xpath("//td[@class='aut']/a/text()").extract()[0]
        pass
