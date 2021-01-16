from lxml.etree import Element


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
