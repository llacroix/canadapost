from lxml.etree import Element

from .base import CPObject, TextField, ObjectField
from .domestic import Domestic


class Destination(CPObject):
    _name = 'destination'

    _fields = {
        "domestic": ObjectField('domestic', format=Domestic),
    }
