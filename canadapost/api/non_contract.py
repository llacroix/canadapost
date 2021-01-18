from .base import BaseApi, method
from ..https import Methods
from ..objects.non_contract_shipment_info import NonContractShipmentInfo


class NonContract(BaseApi):

    @method(
        '/rs/%(customer_no)s/ncshipment',
        'application/vnd.cpc.ncshipment-v4+xml',
        xmlns='http://www.canadapost.ca/ws/ncshipment-v4',
        method=Methods.POST
    )
    def create_shipment(self, data, ns):
        node = self.parse_xml(data)
        return NonContractShipmentInfo.from_xml(node)
