import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChangeListConsumer(AsyncWebsocketConsumer):
    room_name = 'admin'
    room_group_name = f'chat_{room_name}'

    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        """
        Leave a room
        """
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'admin_event',
                'message': message
            }
        )

    async def admin_event(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
