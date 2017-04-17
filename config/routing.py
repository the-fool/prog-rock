from channels.routing import include

channel_routing = [
    include('progrock.routing.public_routing', path=r'^/prog/'),
    include('progrock.routing.internal_routing')
]
