from .base import BaseApi, method
from ..https import Methods
from ..objects.price_quotes import PriceQuotes


class NonContractShipping(BaseApi):

    @method(
        '/rs/ship/price',
        'application/vnd.cpc.ship.rate-v4+xml',
        xmlns='http://www.canadapost.ca/ws/ship/rate-v4',
        method=Methods.POST
    )
    def get_rates(self, data, ns):
        node = self.parse_xml(data)
        return PriceQuotes.from_xml(node)
