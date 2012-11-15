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

'''Displays a helpful help message full of help.'''

__matcher__ = '%NICK.*help'

def respond(brain, user, message, groups):
    yield 'name\t| description\t| regex'
    for script in brain.bot_info['scripts']:
        name = script.__name__.split('.')[-1]
        regex = script.__matcher__.replace('%NICK', brain.bot_info['nick'])
        doc = script.__doc__ if script.__doc__ is not None else '\t\t'
        yield '%s\t| %s\t| %s' % (name, doc, regex)

