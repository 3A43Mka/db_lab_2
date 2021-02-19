from lxml import etree
from scrapy import Selector
from scrapy.spiders import Spider, Request
from urllib.parse import urljoin


class RepkaSpider(Spider):
    name = 'repka'
    start_urls = ['https://repka.ua/products/noutbuki/?brands=73&p=2,']
    max_pages = 20
    filename = 'output/repka.xml'

    def parse(self, response):
        links = Selector(response=response).xpath("//div[@class='product-item-name']/a/@href").getall()[:RepkaSpider.max_pages]
        for link in links:
            yield Request(url=urljoin(response.url, link), callback=self.parse_laptops)

    def parse_laptops(self, response):
        selector = Selector(response=response)
        yield {
            'name': selector.xpath("//h1[@class='page-title']/span//text()").get(),
            'price': selector.xpath("//span[@class='price-wrapper']/@data-price-amount").get(),
            'image': selector.xpath("//img[@class='fotorama__img']/@src").get(),
            'description': selector.xpath("normalize-space(//div[@id='product_description']/div[@class='box'])").get()
        }

    @staticmethod
    def create_xhtml():
        parsed = etree.parse(RepkaSpider.filename)
        template = etree.parse('template.xsl')
        transform = etree.XSLT(template)
        table = transform(parsed)
        with open('output/table.xhtml', 'w') as f:
            f.write(etree.tostring(table, pretty_print=True).decode())
