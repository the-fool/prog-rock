from channels.routing import route
from .consumers import ws_receive, ws_connect, worker

public_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_receive),
]

internal_routing = [
    route('prog-rocker', worker)
]
