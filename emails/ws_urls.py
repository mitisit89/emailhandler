from django.urls import path
from emails import consumer, views

ws_urls = [
    path("ws/emails/", costumer.EmailConsumer.as_asgi()),
    path("emails/", views.email_list_view, name="email_list"),
    path("add-email-account/", views.add_email_account, name="add_email_account"),
]
