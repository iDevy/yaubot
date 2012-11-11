# Copyright 2012 Jake Basile
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

