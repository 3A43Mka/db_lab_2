from lxml import etree
from scrapy import exceptions, Selector, Spider, Request
from urllib.parse import urljoin


class KPISpider(Spider):
    name = 'kpi'
    start_urls = ['https://kpi.ua/']
    allowed_domains = ['kpi.ua']
    max_pages = 20
    filename = 'output/kpi.xml'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visited_pages = []

    def parse(self, response):
        if len(self.visited_pages) >= self.max_pages:
            raise exceptions.CloseSpider('Page limit exceeded.')
        if response.url not in self.visited_pages:
            self.visited_pages.append(response.url)
            yield self.parse_page(response)
        urls = Selector(response=response).xpath('//a/@href').getall()
        for url in urls:
            yield Request(url=urljoin(response.url, url), callback=self.parse)

    def parse_page(self, response):
        selector = Selector(response=response)
        text_data = selector.xpath('//h1[contains(@class, \'page-title\')]/span/text() | //div[contains(@class, '
                                   '\'node__content\')]/div/p').getall()
        images = selector.xpath('//img/@src').getall()
        return {
            'url': response.url,
            'text': [t.strip() for t in text_data],
            'images': [response.urljoin(src) for src in images]
        }

    @classmethod
    def get_average_texts_count(cls):
        return etree.parse(cls.filename).xpath("count(//page/fragment[@type='text']) div count(//page)")
