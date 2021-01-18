from lxml import etree
from lxml.etree import Element


def remove_xmlns(root):
    for elem in root.getiterator():
        elem.tag = etree.QName(elem).localname
    etree.cleanup_namespaces(root)


class CPObject(object):
    def make_ns(self, ns):
        return {
            "cp": ns
        }

    def val(self, data, xpath, ns=None):
        return self.elems(data, xpath)[0].text

    def elems(self, data, xpath, ns=None):
        return data.xpath(xpath)

    def parse_xml(self, data):
        node = etree.fromstring(data)
        remove_xmlns(node)
        return node

    @classmethod
    def get_float(cls, node, xpath, ns=None):
        return float(node.find(xpath).text)

    def get_element(self):
        return Element(self._name)
