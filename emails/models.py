from django.db import models


class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    provider = models.CharField(
        max_length=50,
        choices=(
            ("yandex.ru", "Yandex"),
            ("gmail.com", "Gmail"),
            ("mail.ru", "Mail.ru"),
        ),
    )

    def __str__(self):
        return self.email


class EmailMessage(models.Model):
    account = models.ForeignKey(
        EmailAccount, on_delete=models.CASCADE, related_name="messages"
    )
    subject = models.CharField(max_length=255)
    sent_date = models.DateTimeField()
    received_date = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True)
    attachments = models.JSONField(max_length=1000)

    def __str__(self):
        return f"{self.subject} ({self.sent_date})"
