import requests
import random

__matcher__ = '%NICK.*make me aww.*'

def respond(brain, user, message, groups):
    result = requests.get('http://reddit.com/r/aww.json')
    if result.status_code != 200:
        return 'Cute appropriation failed.'
    cute_images = [
        str(c['data']['url'])
        for c in result.json['data']['children']
        if not c['data']['url'].endswith(u'.gif')
    ]
    return random.choice(cute_images)

