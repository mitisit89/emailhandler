from django.db import transaction
from imap_tools import MailBox

from emails.models import EmailMessage, EmailAccount

def list_of_attachments(msg):
        attachments=[]
        for att in msg:
            attachments.extend((att.filename,
            att.filename,
            att.content_type ,
            att.size))
        return attachments

def import_emails(account:EmailAccount)->None:

    if account.provider == "gmail.com":
        mail = "imap.gmail.com"
    elif account.provider == "yandex.ru":
        mail = "imap.yandex.com"
    elif account.provider == "mail.ru":
        mail = "imap.mail.ru"
    else:
        return

    with MailBox(mail).login(username=account.email, password=account.password) as mailbox:
        for msg in mailbox.fetch(limit=100):
            with transaction.atomic():
                EmailMessage.objects.create(
                    account=account,
                    subject=msg.subject,
                    sent_date=msg.date,
                    body=msg.html or msg.text,
                    attachments=list_of_attachments(msg.attachments)
                )


