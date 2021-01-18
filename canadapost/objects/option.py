from .base import CPObject, TextField, ObjectField
from .qualifier import Qualifier


class Option(CPObject):
    _name = 'option'

    _fields = {
        "code": TextField('option-code'),
        "name": TextField('option-name'),
        "price": TextField('option-price'),
        "amount": TextField('option-amount'),
        "qualifier": ObjectField('qualifier', format=Qualifier),
    }
