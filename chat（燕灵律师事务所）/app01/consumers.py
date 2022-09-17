from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


phone_set = set()


class ChatConsumer(WebsocketConsumer):
    global phone_set

    def websocket_connect(self, message):
        self.accept()
        group = self.scope['url_route']['kwargs'].get('group')
        phone_set.add(group)
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)

    def websocket_receive(self, message):
        group = self.scope['url_route']['kwargs'].get('group')
        pk = self.scope['url_route']['kwargs'].get('id')
        if pk == "客服":
            message['text'] = "{pk}:{text}".format(pk=pk, text=message['text'])
            async_to_sync(self.channel_layer.group_send)(group, {"type": "xx", "message": message})
        else:
            message['text'] = "{pk}:{text}".format(pk=group, text=message['text'])
            async_to_sync(self.channel_layer.group_send)(group, {"type": "xx", "message": message})

    def xx(self, event):
        text = event["message"]["text"]
        self.send(text)

    def websocket_disconnect(self, message):
        try:
            group = self.scope['url_route']['kwargs'].get('group')
            async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
            if group:
                phone_set.remove(group)
            raise StopConsumer()
        except KeyError:
            pass
        except Exception as e:
            raise StopConsumer()
