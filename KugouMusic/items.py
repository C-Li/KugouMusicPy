# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '搜索结果'
    singer_name = scrapy.Field()
    file_name = scrapy.Field()
    song_name = scrapy.Field()
    album_name = scrapy.Field()
    # 320kbps
    hash_320 = scrapy.Field()
    key_320 = scrapy.Field()
    filesize_320 = scrapy.Field()
    ext_320 = scrapy.Field()
    url_320 = scrapy.Field()
    bitRate_320 = scrapy.Field()

    # SQ
    hash_sq = scrapy.Field()
    key_sq = scrapy.Field()
    filesize_sq = scrapy.Field()
    ext_sq = scrapy.Field()
    url_sq = scrapy.Field()
    bitRate_sq = scrapy.Field()
