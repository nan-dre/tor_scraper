import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VersuriSpider(CrawlSpider):
    name = "versuri"
    allowed_domains = ["versuri.ro"]
    start_urls = [
        "https://www.versuri.ro/artist/costel-biju-_83p.html#",
    ]
    rules = [Rule(LinkExtractor(allow='versuri/'), callback='parse_item', follow=True)]
    # def __init__(self, *args, **kwargs):
    #     super(scrapy.Spider, self).__init__(*args, **kwargs)
    #     with open("links.txt", 'r') as f:
    #         self.start_urls = f.read().splitlines()


    def parse_item(self, response):
        yield {
            'title': response.xpath('//blockquote/h1/text()').get(),
            'lyrics': response.xpath('//blockquote/text()').getall(),
        }
