import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer
import threading
from emails.models import EmailAccount,EmailMessage
from channels.db import database_sync_to_async

import json
from channels.generic.websocket import WebsocketConsumer
from .models import EmailAccount, EmailMessage
from .utils import import_emails


class EmailConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for account in EmailAccount.objects.all().iterator():
            import_emails(account)
        self.send_progress(0, 'Reading messages...')
        for i,msg in enumerate(EmailMessage.objects.all().iterator()):
                self.send_message(
                    {'id': i, 'subject': msg.subject, 'sent_date':str(msg.sent_date), 'received_date':str(msg.received_date), 'snippet': msg.body,
                     'attachments': msg.attachments})
                self.send_progress(i, 'Fetching messages' if i < 50 else 'Loading messages')

    def send_progress(self, progress, message):
        self.send(text_data=json.dumps({
            'type': 'progress',
            'progress': progress,
            'message': message
        }))

    def send_message(self, message):
        self.send(text_data=json.dumps({
            'type': 'new_message',
            'message': message
        }))


