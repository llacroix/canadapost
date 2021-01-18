from .base import CPObject, TextField, ObjectField
from .address_details import AddressDetails


class Sender(CPObject):
    _name = 'sender'

    _fields = {
        "name": TextField("name"),
        "company": TextField("name"),
        "contact_phone": TextField("contact-phone"),
        "address_details": ObjectField("address-details", AddressDetails),
    }
