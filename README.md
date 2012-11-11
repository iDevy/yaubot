# Yaubot

Frustrated with Hubot being terrible to install? Try **Yet Another Unnecessary Bot**!

## Installation

    $ git clone https://github.com/jakebasile/yaubot.git
    $ cd yaubot
    $ virtualenv env && source env/bin/activate
    $ pip install -r requirements.txt

That's it. Move on to the next section.

## Configuration

Currently Yaubot only supports IRC. To set that up:

    $ export YAUBOT_IRC_SERV=irc.derpnet.org \
        YAUBOT_IRC_PORT=6667 \
        YAUBOT_IRC_CHANS='#derp,#derp2' \
        YAUBOT_NAME='jarvis'
    $ ./yaubot irc

## Scripts

Yaubot works like a low-rent clone of Hubot, because that's what it is. It finds scripts in the `scripts` directory, checks against their `__matcher__` regex and runs them if it matches. Check out any of the included scripts for details.

**Note**: Yaubot must be restarted to recognize new scripts.
