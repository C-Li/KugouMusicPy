# KugouMusicPy
用Scrapy实现的酷狗音乐下载器， 
暂未完成下载，只是把歌曲信息包括下载地址保存在本地json里。  
程序只会获取320K和无损(SQ)的音乐，低码率的会直接忽略。

### 主要工作流程
1. 从关键字搜索接口搜索获得匹配的歌曲信息列表
2. 向下载接口请求下载的文件信息
3. 整合歌曲信息和文件信息保存到本地json文件

### 使用方法

命令行打开到项目文件夹内，执行

    scrapy crawl kugou

开始运行爬虫，运行结束后将会在项目文件夹下生成item.json

### item.json示例

    {
        "song_name": "深海少女",
        "singer_name": "初音ミク",
        "album_name": "EXIT TUNES PRESENTS Vocalodream (ボカロドリーム) feat. 初音ミク",
        "file_name": "初音ミク - 深海少女",

        "hash_320": "a7d0583042b61bec8968bc2b83860d2e",
        "hash_sq": "217a1beeb09a0785a70a370353155079",
        "key_320": "3f1dcbaf50ff9486aad6d64256302433",
        "key_sq": "444058a68263f96259a0c36351cd09b1",

        "filesize_320": 8309388,
        "ext_320": "mp3",
        "url_320": "http://fs.vip.pc.kugou.com/201811151125/6e62c95d8e7f1c2c21887edde2d34308/G002/M09/0E/07/Qg0DAFS62MGAJz0mAH7KjIkrOk0340.mp3",
        "bitRate_320": 320134,

        "filesize_sq": 25374966,
        "ext_sq": "flac",
        "url_sq": "http://fs.vip.pc.kugou.com/201811151125/52d196f2a4be9738f7c7e69c5e13344c/G005/M0A/0C/07/pYYBAFUDozqAc5VZAYMw9q1Rx7884.flac",
        "bitRate_sq": 977000
    }

从上到下分为4部分：
1. 歌曲信息
2. hash和key，用于请求文件下载信息
3. 320K文件信息
4. SQ文件信息

根据歌曲实际情况可能会没有320K或者SQ的相关内容，低与320K码率的音乐则只会有歌曲信息。