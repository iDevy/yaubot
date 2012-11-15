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

'''Provides more information about this bot.'''

__matcher__ = '((what|who) is %NICK|%NICK about)'

def respond(brain, user, message, group):
    return [
        'I am a bot that provides useful and useless functions.',
        'I respond to commands typed into any channel I am present in.',
        'To learn more about what I can do, try asking me for help.',
        'My source code is available at https://github.com/jakebasile/yaubot',
    ]
