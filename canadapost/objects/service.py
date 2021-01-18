from .base import CPObject, TextField


class Service(CPObject):
    _name = 'service'

    _fields = {
        "code": TextField('service-code'),
        "name": TextField('service-name'),
    }
