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

import random
import requests
import unicodedata

__matcher__ = '%NICK,? (quote from (?P<where>\w*)|learn from (?P<learn>.*) as (?P<name>\w*)|forget (?P<forget>.*))'

class Quoterator(object):
    
    def __init__(self, text):
        self.lookback = 3
        self.text = {}
        self.words = text.split()
        for i in xrange(len(self.words) - self.lookback - 1):
            key = tuple(self.words[i+offset] for offset in xrange(1, self.lookback + 1))
            if key not in self.text:
                self.text[key] = [self.words[i + self.lookback + 1]]
            else:
                self.text[key].append(self.words[i + self.lookback + 1])
    
    def quote(self, length=10):
        start = random.randint(0, len(self.words) - self.lookback)
        chain = [self.words[start+i] for i in xrange(self.lookback)]
        while len(chain) < length:
            previous = tuple(
                chain[i]
                for i in xrange(-1 * self.lookback, 0)
            )
            chain.append(random.choice(self.text[previous]))
        return ' '.join(chain)

def respond(brain, user, message, groups):
    if 'where' in groups and groups['where'] is not None:
        where = groups['where']
        if where in brain:
            loc = brain[where]
            results = requests.get(loc)
            if results.status_code != 200:
                return 'Unable to quote right now.'
            q = Quoterator(results.text)
            return unicodedata.normalize('NFKD', q.quote(45)).encode('ascii', 'ignore')
        else:
            return 'I haven\'t learned from that location.'
    elif 'forget' in groups and groups['forget'] is not None:
        del brain[groups['forget']]
        return 'I have forgotten all the things.'
    else:
        name = groups['name']
        learn_loc = groups['learn']
        brain[name] = learn_loc
        return 'I have learned all the things.'

