from asgiref.sync import async_to_async
from channels.generic.websockets import WebsocketConsumer
import json
from .models import AppModel

class AppConsumer(WebsocketConsumer):
    def connection(self):
        self.room_group_name = 'Chat'
        
        async_to_async(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        
        
    def disconnect(self, close_code):
        async_to_async(self, channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
        
    def receive(self, text_data):
        text_data_json = json.load(text_data)
        title = text_data_json['title']
        content = text_data_json['content']
        id = text_data_json['id']
        