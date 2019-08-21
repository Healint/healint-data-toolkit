from lxml import etree


class HTMLParserManager:
    def get_elements_by_xpath(self, content: str, xpath: str):
        parser = etree.HTMLParser()
        tree = etree.parse(content, parser)
        tree.xpath(xpath)
