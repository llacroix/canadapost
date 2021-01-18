from .base import CPObject, TextField, ObjectField


class ParcelCharacteristics(CPObject):
    _name = 'parcel-characteristics'

    _fields = {
        "weight": TextField('weight'),
    }
