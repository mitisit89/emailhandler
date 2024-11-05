import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_importer.settings")
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
from channels.auth import AuthMiddlewareStack

from emails.ws_urls import ws_urls

application = ProtocolTypeRouter({
"http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws_urls,

        )
    ),
})
