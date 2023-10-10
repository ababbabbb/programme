from boot_framework.AppFactory.http import HttpFactory
from boot_framework.AppFactory.websocket import WebsocketFactory


factories = {
    'websocket': WebsocketFactory(),
    'http': HttpFactory()
}
