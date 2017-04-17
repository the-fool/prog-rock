from channels.routing import include

channel_routing = [
    include('progrock.routing.channel_routing', path=r'^/prog')
]
