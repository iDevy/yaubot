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

__matcher__ = '%NICK,? +((?P<who>\w*) is (?P<what>.*)|(describe|tell me about) (?P<query>\w*))'

def respond(brain, user, message, groups):
    if 'query' in groups and groups['query'] is not None:
        who = groups['query'].title()
        if who in brain:
            what = brain[who]
            return '%s is %s' %(who, what)
        else:
            return '%s is nothing to me.' % who
    else:
        who = groups['who'].title()
        what = groups['what']
        brain[who] = what
        return 'Information stored, meatbag.'
