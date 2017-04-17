from channels.routing import route
from .consumers import ws_receive, ws_connect, worker

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.message', ws_receive),
    route('worker', worker)
]
