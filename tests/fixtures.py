import os
import pytest


@pytest.fixture
def canadapost_sync_client():
    from canadapost.client.sync import SyncClient

    url = 'https://ct.soa-gw.canadapost.ca'
    username = os.environ['CP_USERNAME']
    password = os.environ['CP_PASSWORD']
    customer_no = os.environ['CP_CUSTOMER_NO']

    client = SyncClient(url, username, password, customer_no)

    return client


@pytest.fixture
def rating_api(canadapost_sync_client):
    from canadapost.api.rating import Rating
    return Rating(canadapost_sync_client)
