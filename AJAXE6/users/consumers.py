import json
from .models import *
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
       self.accept() # Принимает все соединения

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        chat_id = text_data_json["chat_id"]

        if command == 'send':
            message = text_data_json["message"]
            

            new_message = Message.objects.create(
                text=message,
                sender=self.scope['user'],
                chat=Chat.objects.get(id=chat_id)
            )

            message_dict = {
                'message': new_message.text,
                'sender': new_message.sender.first_name,
                'by_request_user': True,
                'image' : new_message.sender.avatar.url
            }

            send_dict = {
                'message': [message_dict]
            }


            self.send(text_data=json.dumps(send_dict))
        
        elif command == 'load':
            list_queryset = list(Message.objects.filter(chat=Chat.objects.get(id=chat_id)))

            send_dict = {
                'message': []
            }

            for item in list_queryset:
                message_dict = {
                    'message': item.text,
                    'sender': item.sender.first_name,
                    'by_request_user': True if item.sender == self.scope['user'] else False,
                    'image' : item.sender.avatar.url
                }

                print(message_dict)

                send_dict['message'].append(message_dict)

            self.send(text_data=json.dumps(send_dict))
            



            


