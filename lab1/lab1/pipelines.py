from lxml import etree
from lab1.spiders.kpi_spider import KPISpider
from lab1.spiders.repka_spider import RepkaSpider


def new_element(parent, tag, attrib={},
                text=None, nsmap=None, **_extra):
    el = etree.SubElement(parent, tag, attrib, nsmap, **_extra)
    el.text = text
    return el


class MyPipeline(object):
    def __init__(self):
        self.data = None
        self.doc = None

    def open_spider(self, spider):
        self.data = etree.Element('data')
        self.doc = etree.ElementTree(self.data)

    def close_spider(self, spider):
        self.doc.write(spider.filename, xml_declaration=True,
                       encoding='utf-8', pretty_print=True)

    def process_item(self, item, spider):
        if isinstance(spider, KPISpider):
            self.process_kpiua_item(item)
        elif isinstance(spider, RepkaSpider):
            self.process_repka_item(item)

    def process_kpiua_item(self, item):
        page = etree.Element('page', url=item['url'])
        for text in item['text']:
            if text:
                new_element(page, 'fragment', type='text', text=text)
        for src in item['images']:
            new_element(page, 'fragment', type='image', text=src)
        self.data.append(page)

    def process_repka_item(self, item):
        laptop = etree.Element('laptop', name=item.pop('name'))
        for key, value in item.items():
            new_element(laptop, key, text=value)
        self.data.append(laptop)