from .base import CPObject
from .adjustment import Adjustment


class Adjustments(CPObject):
    _name = 'adjustments'

    def __init__(self, adjustments):
        self.adjustments = {
            adjustment.code: adjustment
            for adjustment in adjustments
        }

    @classmethod
    def from_xml(cls, node, ns):
        adjustments = [
            Adjustment.from_xml(adjustment, ns)
            for adjustment in node.xpath(
                './/cp:adjustment', namespaces=ns
            )
        ]

        return Adjustments(adjustments)

    def to_xml(self):
        elem = self.get_element()

        for adjustment in self.adjustments.values():
            elem.append(adjustment.to_xml())

        return elem
