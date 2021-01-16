from ..https import Methods
from .base import Client
from aiohttp import ClientSession


class SyncClient(Client):

    def send_request(self, request):
        url = self.make_url(request)

        async def handle_request(request):
            if not self.session:
                self.session = await ClientSession()

            if request.method == Methods.POST:
                response = await self.session.post(
                    url,
                    params=request.query,
                    data=request.data,
                    headers=request.headers,
                    auth=(self.username, self.password)
                )
            elif request.method == Methods.GET:
                response = await self.session.post(
                    url,
                    params=request.query,
                    data=request.data,
                    headers=request.headers,
                    auth=(self.username, self.password)
                )

            content = await response.read()

            if response.status == 500:
                return self.map_server_error(content)

            return request.map(content)

        return handle_request(request)
