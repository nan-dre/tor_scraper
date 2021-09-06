import scrapy


class VersuriSpider(scrapy.Spider):
    name = "versuri"
    def __init__(self, *args, **kwargs):
        super(scrapy.Spider, self).__init__(*args, **kwargs)
        with open("links.txt", 'r') as f:
            self.start_urls = f.read().splitlines()


    def parse(self, response):
        print("Link: " + response.url)
        print("Title: " + response.xpath('//blockquote/h1/text()').get())
        print()
        yield {
            'title': response.xpath('//blockquote/h1/text()').get(),
            'lyrics': response.xpath('//blockquote/text()').getall(),
        }
