from lxml import etree

import pytest
from fixtures import *


def test_create_shipment(non_contract_api):
    from canadapost.objects.non_contract_shipment import NonContractShipment
    from canadapost.objects.non_contract_shipment_info import (
        NonContractShipmentInfo
    )
    from canadapost.objects.delivery_spec import DeliverySpec
    from canadapost.objects.destination import Destination
    from canadapost.objects.sender import Sender
    from canadapost.objects.address_details import AddressDetails
    from canadapost.objects.parcel_characteristics import ParcelCharacteristics
    from canadapost.objects.preferences import Preferences

    shipment = NonContractShipment(
        delivery_spec=DeliverySpec(
            service_code='DOM.RP',
            sender=Sender(
                company='Canada Post',
                contact_phone='',
                address_details=AddressDetails(
                    line_1='1000 3e Ave',
                    city='Québec',
                    prov_state='QC',
                    postal_zip_code='G1L2X0'
                )
            ),
            destination=Destination(
                name='Montréal',
                address_details=AddressDetails(
                    line_1='2000 Boulevard Marcel-Laurin',
                    city='Saint-Laurent',
                    prov_state='QC',
                    postal_zip_code='H4R1J0',
                    country_code='CA',
                )
            ),
            parcel_characteristics=ParcelCharacteristics(
                weight=1
            ),
            preferences=Preferences(
                show_packing_instructions=True
            ),
        )
    )

    shipment_info = non_contract_api.create_shipment(
        etree.tostring(shipment.to_xml(set_xmlns=True)).decode(),
    )

    assert isinstance(shipment_info, NonContractShipmentInfo) is True
