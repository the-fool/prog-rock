from channels import Channel
from channels.sessions import channel_session

import json


@channel_session
def ws_connect(msg):
    msg.reply_channel.send({'text': json.dumps({"accept": True})})


@channel_session
def ws_receive(message):
    print(message)
    data = json.loads(message['text'])
    reply_channel = message.reply_channel.name

    if data['action'] == 'start':
        Channel('prog-rocker').send({
            'reply_channel': reply_channel,
            'command': 'start',
        })


def worker(msg):
    def delayed_message(reply_channel, progress, command='continue'):
        return {
            'channel': 'prog-rocker',
            'content': {
                'reply_channel': reply_channel,
                'command': command,
                'progress': progress,
            },
            'delay': 200
        }

    def delayed_send(msg):
        Channel('asgi.delay').send(msg, immediately=True)

    def send_to_ws(reply_channel, content):
        Channel(reply_channel).send({'text': json.dumps(content)})

    def send_progress(reply_channel, progress):
        send_to_ws(reply_channel, {'progress': progress})

    cmd = msg.content['command']
    reply = msg.content['reply_channel']

    if cmd == 'start':
        # start a long running background task!
        progress = 0
        send_progress(reply, progress)

        new_msg = delayed_message(reply, progress)
        delayed_send(new_msg)

    elif cmd == 'continue':
        # check in on the background task
        progress = msg.content['progress'] + 3
        if progress >= 100:
            send_to_ws(reply, {'complete': True, 'progress': 100})
        else:
            command = 'continue'
            send_progress(reply, progress)
            new_msg = delayed_message(reply, progress, command)
            delayed_send(new_msg)
