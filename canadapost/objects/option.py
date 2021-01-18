from .base import CPObject


class Option(CPObject):
    _name = 'option'

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    @classmethod
    def from_xml(cls, node):
        code = node.find('option-code').text
        name = node.find('option-name').text
        price = node.find('option-price').text
        price = float(price)
        return Option(code, name, price)
