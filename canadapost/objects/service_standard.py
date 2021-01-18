from .base import CPObject
from lxml.etree import Element
from datetime import datetime


class ServiceStandard(CPObject):
    _name = 'service-standard'

    def __init__(
        self,
        am_delivery,
        guaranteed_delivery,
        expected_transit_time,
        expected_delivery_date
    ):
        self.am_delivery = am_delivery
        self.guaranteed_delivery = guaranteed_delivery
        self.expected_transit_time = expected_transit_time
        self.expected_delivery_date = expected_delivery_date

    @classmethod
    def from_xml(cls, node, ns):
        am_delivery = node.find('cp:am-delivery', namespaces=ns).text
        am_delivery = am_delivery == 'true'

        guaranteed_delivery = node.find('cp:guaranteed-delivery', namespaces=ns).text
        guaranteed_delivery = guaranteed_delivery == 'true'

        expected_transit_time = node.find('cp:expected-transit-time', namespaces=ns).text
        expected_transit_time = float(expected_transit_time)

        expected_delivery_date = node.find('cp:expected-delivery-date', namespaces=ns).text
        expected_delivery_date = datetime.strptime(expected_delivery_date, '%Y-%m-%d')

        return ServiceStandard(
            am_delivery,
            guaranteed_delivery,
            expected_transit_time,
            expected_delivery_date
        )

    def to_xml(self):
        elem = self.get_element()

        am_delivery = Element('am-delivery')
        am_delivery.text = 'true' if self.am_delivery else 'false'

        guaranteed_delivery = Element('guaranteed-delivery')
        guaranteed_delivery.text = (
            'true'
            if self.guaranteed_delivery
            else 'false'
        )

        expected_transit_time = Element('expected-transit-time')
        expected_transit_time.text = str(self.expected_transit_time)

        expected_delivery_date = Element('expected-delivery-date')
        expected_delivery_date.text = self.expected_delivery_date.strftime(
            '%Y-%m-%d'
        )

        elem.append(am_delivery)
        elem.append(guaranteed_delivery)
        elem.append(expected_transit_time)
        elem.append(expected_delivery_date)

        return elem
