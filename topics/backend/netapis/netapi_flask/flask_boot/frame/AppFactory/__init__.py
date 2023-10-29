from frame.AppFactory.http import HttpFactory
from frame.AppFactory.websocket import WebsocketFactory


factories = {
    'websocket': WebsocketFactory(),
    'http': HttpFactory()
}
