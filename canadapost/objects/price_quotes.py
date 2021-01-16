from .base import CPObject
from .price_quote import PriceQuote


class PriceQuotes(CPObject):
    _name = 'price-quotes'

    def __init__(self, quotes):
        self.quotes = {
            quote.code: quote
            for quote in quotes
        }

    @classmethod
    def from_xml(cls, node, ns):
        quotes = [
            PriceQuote.from_xml(quote_node, ns)
            for quote_node in node.xpath('.//cp:price-quote', namespaces=ns)
        ]

        return PriceQuotes(quotes)

    def to_xml(self):
        elem = self.get_element()

        for quote in self.quotes.values():
            quote_node = quote.to_xml()
            elem.append(quote_node)

        return elem
