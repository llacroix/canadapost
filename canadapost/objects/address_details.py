from .base import CPObject, TextField


class AddressDetails(CPObject):
    _name = 'address-details'

    _fields = {
        # NonContractShipping
        "line-1": TextField("address-line-1"),
        "line-2": TextField("address-line-2"),
        "city": TextField("city"),
        "country_code": TextField("country-code"),
        "postal_zip_code": TextField("postal-zip-code"),
        "prov_state": TextField("prov-state"),
    }
