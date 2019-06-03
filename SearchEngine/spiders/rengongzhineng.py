# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from scrapy.http import Request
from urllib import parse
import time
from SearchEngine.items import AIArticleItem
from SearchEngine.utils.common import get_md5


class RengongzhinengSpider(scrapy.Spider):
    name = 'rengongzhineng'
    allowed_domains = ['www.leiphone.com']
    # start_urls = ['http://www.leiphone.com/']
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

        post_nodes = response.css(".box div")
        print(type(post_nodes))
        for post_node in post_nodes:

            image_url = post_node.css("img::attr(src)").extract_first("")
            print(image_url)
            post_url = post_node.css("h3 a::attr(href)").extract_first("")
            print(post_url)
            # yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
            #               callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        # next_url = response.css(".next::attr(href)").extract()[1]
        # next_url = parse.urljoin(response.url, next_url)
        # if next_url:
        #     yield Request(url=next_url, callback=self.parse)

    @decorate
    def parse_detail(self, response):

        article_item = AIArticleItem()

        # 提取文章的具体字段

        title = response.xpath('/html/body/div[6]/div[1]/div[1]/div/h1/text()').extract_first("").strip()
        print(title)

        abstract = response.xpath("/html/body/div[6]/div[1]/div[1]/div/div[2]/text()").extract()[1].strip()
        content = response.xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div[1]").extract_first("")
        create_date = response.xpath("//td[@class='time']/text()").extract_first("").strip()
        author = response.xpath("//td[@class='aut']/a/text()").extract_first("")

        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        article_item["abstract"] = abstract
        article_item["front_image_url"] = [front_image_url]
        article_item["content"] = content
        article_item["create_date"] = create_date
        article_item["author"] = author
        # 传入pipelines
        yield article_item
