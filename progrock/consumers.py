from channels import Channel
from channels.sessions import channel_session

import json


# Connected to websocket.connect
@channel_session
def ws_connect(msg):
    msg.reply_channel.send({
        'text': json.dumps({"accept": True})
    })


@channel_session
def ws_receive(message):
    data = json.loads(message['text'])
    reply_channel = message.reply_channel.name

    if data['action'] == 'start':
        Channel('worker').send({
            'reply_channel': reply_channel,
            'command': 'start'
        })


def worker(message):
    pass
