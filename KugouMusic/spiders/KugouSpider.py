import scrapy
import json
import hashlib  # md5
from scrapy.spiders import Spider
from scrapy.utils.response import open_in_browser
from KugouMusic.items import SearchItem


# 查询api 填入keyword和page
searchUrl = "http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword=%s&page=%d&pagesize=100"
# 下载api 填入hash和 (hash+'kgcloud')的MD5值
downloadUrl = 'http://trackercdn.kugou.com/i/?cmd=4&hash=%s&key=%s&pid=1&forceDown=0&vip=1'


class KugouSpider(Spider):
    name = "kugou"

    # 计算key值，下载用
    def getKey(self, hashstr):
        hl = hashlib.md5()
        hl.update((hashstr+'kgcloud').encode("utf-8"))
        result = hl.hexdigest()
        return result

    # 请求歌曲列表
    def start_requests(self):
        # 指定 parse 作为回调函数并返回 Requests 请求对象
        for page in range(1, 2):
            yield scrapy.Request(url=searchUrl % ('初音', page), callback=self.parse)

    # 解析json获取歌曲信息
    def parse(self, response):

        body = json.loads(response.body_as_unicode())
        for info in body['data']['info']:
            item = SearchItem()
            yes_320 = False   # 标记有没有320hash
            yes_sq = False    # 标记sqhash
            item['song_name'] = info['songname']
            item['singer_name'] = info['singername']
            item['album_name'] = info['album_name']
            item['file_name'] = info['filename']
            # 如果没有320K的歌就跳过这部分
            if info['320hash'] != '':
                item['hash_320'] = info['320hash']
                item['key_320'] = self.getKey(item['hash_320'])
                yes_320 = True
            # 如果没有SQ的歌就跳过这部分
            if info['sqhash'] != '':
                item['hash_sq'] = info['sqhash']
                item['key_sq'] = self.getKey(item['hash_sq'])
                yes_sq = True

            if yes_320:
                yield scrapy.Request(url=downloadUrl % (item['hash_320'], item['key_320']), meta={'item': item, 'yes_sq': yes_sq}, callback=self.detail_parse)
            elif yes_sq:
                yield scrapy.Request(url=downloadUrl % (item['hash_sq'], item['key_sq']), meta={'item': item}, callback=self.detail_parse2)
            else:
                yield item

    # 320K
    def detail_parse(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        yes_sq=response.meta['yes_sq']

        body = json.loads(response.body_as_unicode())
        item['filesize_320'] = body['fileSize']
        item['ext_320'] = body['extName']
        item['url_320'] = body['url']
        item['bitRate_320'] = body['bitRate']

        if yes_sq:
            yield scrapy.Request(url=downloadUrl % (item['hash_sq'], item['key_sq']), meta={'item': item}, callback=self.detail_parse2)
        else:
            yield item

    # SQ
    def detail_parse2(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']

        body = json.loads(response.body_as_unicode())
        item['filesize_sq'] = body['fileSize']
        item['ext_sq'] = body['extName']
        item['url_sq'] = body['url']
        item['bitRate_sq'] = body['bitRate']

        yield item
