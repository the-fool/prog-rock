from channels import Channel
import json


def ws_connect(msg):
    msg.reply_channel.send({'text': json.dumps({"accept": True})})


def ws_receive(message):
    print(message)
    data = json.loads(message['text'])
    reply_channel = message.reply_channel.name

    if data['action'] == 'start':
        Channel('prog-rocker').send({
            'reply_channel': reply_channel,
            'action': 'start',
        })


def worker(msg):
    def delayed_message(reply_channel, progress, action):
        return {
            'channel': 'prog-rocker',
            'content': {
                'reply_channel': reply_channel,
                'action': action,
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

    action = msg.content['action']
    reply = msg.content['reply_channel']

    if action == 'start':
        # start a long running background task!
        # (this is just a mockup, using number to represent the progress of a background task)
        progress = 0

        send_progress(reply, progress)

        new_msg = delayed_message(reply, progress, 'continue')
        delayed_send(new_msg)

    elif action == 'continue':
        # check in on the background task
        # (we are simulating a task by incrementing a number)
        progress = msg.content['progress'] + 3
        if progress >= 100:
            send_to_ws(reply, {'complete': True, 'progress': 100})
        else:
            send_progress(reply, progress)
            new_msg = delayed_message(reply, progress, 'continue')
            delayed_send(new_msg)
