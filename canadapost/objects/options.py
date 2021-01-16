from .base import CPObject
from .option import Option


class Options(CPObject):
    _name = 'options'

    def __init__(self, options):
        self.options = {
            option.code: option
            for option in options
        }

    @classmethod
    def from_xml(cls, node, ns):
        options = [
            Option.from_xml(option, ns)
            for option in node.xpath(
                './/cp:option', namespaces=ns
            )
        ]

        return Options(options)
