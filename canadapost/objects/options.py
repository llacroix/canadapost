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
    def from_xml(cls, node):
        options = [
            Option.from_xml(option)
            for option in node.xpath('.//option')
        ]

        return Options(options)
