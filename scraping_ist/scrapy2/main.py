import scrapy


class MySpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['http://github.com']
    start_urls = [
        'http://github.com/oshou'
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}
