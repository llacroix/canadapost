from lxml import etree
from lxml.etree import Element


def remove_xmlns(root):
    for elem in root:
        elem.tag = etree.QName(elem).localname
    etree.cleanup_namespaces(root)


class CPObject(object):
    def make_ns(self, ns):
        return {
            "cp": ns
        }

    def val(self, data, xpath, ns):
        return self.elems(data, xpath, ns)[0].text

    def elems(self, data, xpath, ns):
        return data.xpath(xpath, namespaces=ns)

    @classmethod
    def get_float(cls, node, xpath, ns):
        return float(node.find(xpath, namespaces=ns).text)

    def get_element(self):
        return Element(self._name)
