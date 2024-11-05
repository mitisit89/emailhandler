
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('emails.urls')),
path('', lambda request: redirect('add-email-account/', permanent=True)),

]
