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

from twisted.internet import protocol, reactor, ssl
from twisted.words.protocols import irc
import os

class IRCAdapter(irc.IRCClient):

    @property
    def nickname(self):
        return self.factory.nick

    @property
    def password(self):
        return self.factory.password

    def signedOn(self):
        for chan in self.factory.chans:
            self.join(chan)

    def privmsg(self, user, channel, message):
        user_nick = user.split('!')[0]
        response = self.factory.bot.proc(user_nick, message)
        if response is not None and response != '':
            if isinstance(response, basestring):
                self.say(channel, response)
            else:
                map(lambda r: self.say(channel, r) if r is not None else None, response)

class IRCAdapterFactory(protocol.ClientFactory):
    protocol = IRCAdapter

    def __init__(self, nick, chans, bot, password=None):
        self.bot = bot
        self.nick = nick
        self.password = password
        self.chans = chans

def run(bot):
    serv = os.environ['YAUBOT_IRC_SERV']
    port = int(os.environ['YAUBOT_IRC_PORT'])
    nick = bot.nick
    password = os.environ.get('YAUBOT_IRC_PASSWORD', None)
    chans = os.environ['YAUBOT_IRC_CHANS'].split(',')
    if os.environ.get('YAUBOT_IRC_SSL', 'False') == 'True':
        reactor.connectSSL(
            serv,
            port,
            IRCAdapterFactory(nick, chans, bot, password=password),
            ssl.ClientContextFactory(),
        )
    else:
        reactor.connectTCP(
            serv,
            port,
            IRCAdapterFactory(nick, chans, bot, password=password),
        )
    reactor.run()
    
