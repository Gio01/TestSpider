import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        urls=[

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split('/')[-2]
        print(page)
