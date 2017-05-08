#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  messenger-bot - app.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/8/17
#  Time: 10:30 AM
#
#

import yaml
import requests

from sanic import Sanic
from sanic.response import text, json

app = Sanic()

with open('config.yaml', 'r') as ymlfile:
    conf = yaml.load(ymlfile)


def reply(user_id, msg):
    data = {
        'recipient': {'id': user_id},
        'message': {'text': msg}
    }
    resp = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=' + conf['ACCESS_TOKEN'], json=data)
    json(resp.content)


@app.route('/', methods=['GET'])
def handle_verification(request):
    if request.args['hub.verify_token'][0] == conf['VERIFY_TOKEN']:
        return text(request.args['hub.challenge'][0])
    else:
        return text('Invalid verification token')


@app.route('/', methods=['POST'])
def handle_incoming_messages(request):
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
