import json
import pytest
from channels.testing import WebsocketCommunicator
from realtime_admin.core.consumers import ChangeListConsumer


@pytest.mark.asyncio
async def test_can_connect_to_websocket():
    communicator = WebsocketCommunicator(ChangeListConsumer, 'ws/list')
    connected, subprotocol = await communicator.connect()
    assert connected
    assert subprotocol is None
    await communicator.send_to(text_data=json.dumps({
                'type': 'admin_event',
                'product': 'product',
                'client': 'client',
                'value': 'value'
            }))
    message = await communicator.receive_from()
    for field in ('product', 'client', 'value'):
        assert field in message


@pytest.mark.asyncio
async def test_can_send_message_to_websocket():
    communicator = WebsocketCommunicator(ChangeListConsumer, 'ws/list')
    await communicator.connect()
    await communicator.send_to(text_data=json.dumps({
        'type': 'admin_event',
        'product': 'product',
        'client': 'client',
        'value': 'value'
    }))
    message = await communicator.receive_from()
    for field in ('product', 'client', 'value'):
        assert field in message
