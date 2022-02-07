import scrapy


class Icourse163Spider(scrapy.Spider):
    name = 'icourse163' #爬虫名
    allowed_domains = ['icourse163.org'] #允许爬取的范围
    start_urls = ['http://icourse163.org/'] #最开始请求的url地址

    def parse(self, response):
        # 处理start_urls地址对应的响应

        pass
