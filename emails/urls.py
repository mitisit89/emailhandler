from django.urls import path

from emails import views

urlpatterns = [
    path('emails/', views.email_list_view, name='email_list'),
path('add-email-account/', views.add_email_account, name='add_email_account'),
]
