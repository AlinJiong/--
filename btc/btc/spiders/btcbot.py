import scrapy


class BtcbotSpider(scrapy.Spider):
    name = 'btcbot'
    allowed_domains = ['btc.com']
    start_urls = ['https://btc.com/zh-CN/btc/top-address']

    def parse(self, response):
        filename = "add.html"
        open(filename, 'w').write(response.body)
