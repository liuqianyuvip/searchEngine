# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from SearchEngine.models import ArticleType


class SearchengineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AIArticleItem(scrapy.Item):
    channel = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    abstract = scrapy.Field()
    create_date = scrapy.Field()

    # front_image_url = scrapy.Field()
    # front_image_path = scrapy.Field()

    origin_url = scrapy.Field()

    url_object_id = scrapy.Field()

    def save_to_es(self):

        article_type = ArticleType()
        # url = Keyword()
        # title = Text(analyzer="ik_max_word")
        # channel = Text()
        # content = Text(analyzer="ik_max_word")
        # author = Text()
        # abstract = Text(analyzer="ik_max_word")
        # create_date = Date()
        article_type.origin_url = self["origin_url"]
        article_type.title = self["title"]
        article_type.channel = self["channel"]
        article_type.content = self["content"]
        article_type.author = self["author"]
        article_type.abstract = self["abstract"]
        article_type.create_date = self["create_date"]
        article_type.title_suggest = self["title"]
        article_type.abstract_suggest =self["abstract"]
        article_type.content_suggest = self["content"]
        article_type.save()
        return





