from lxml.etree import Element

from .base import CPObject, TextField, ObjectField
from .adjustment_qualifier import AdjustmentQualifier


class Adjustment(CPObject):
    _name = 'adjustment'

    _fields = {
        "code": TextField('adjustment-code'),
        "name": TextField('adjustment-name'),
        "qualifier": ObjectField(
            'adjustment-qualifier', format=AdjustmentQualifier
        ),
    }

#   def __init__(self, code, name, qualifier):
#       self.code = code
#       self.name = name
#       self.qualifier = qualifier
#
#   @classmethod
#   def from_xml(cls, node):
#       code = node.find('adjustment-code').text
#       name = node.find('adjustment-name').text
#       qualifier = {}
#
#       if len(node.xpath('.//adjustment-qualifier/percent')) > 0:
#           percent = node.xpath('.//percent')[0].text
#           qualifier['percent'] = float(percent)
#
#       return Adjustment(
#           code,
#           name,
#           qualifier
#       )
#
#   def to_xml(self):
#       elem = self.get_element()
#
#       code = Element('adjustment-code')
#       code.text = self.code
#
#       name = Element('adjustment-name')
#       name.text = self.name
#
#       elem.append(code)
#       elem.append(name)
#
#       return elem
