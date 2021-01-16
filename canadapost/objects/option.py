from .base import CPObject


class Option(CPObject):
    _name = 'option'

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    @classmethod
    def from_xml(cls, node, ns):
        code = node.find('cp:option-code', namespaces=ns).text
        name = node.find('cp:option-name', namespaces=ns).text
        price = node.find('cp:option-price', namespaces=ns).text
        price = float(price)
        return Option(code, name, price)
