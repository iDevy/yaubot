__matcher__ = '((what|who) is %NICK|%NICK about)'

def respond(brain, user, message, group):
    return [
        'I am a bot that provides useful and useless functions.',
        'I respond to commands typed into any channel I am present in.',
        'To learn more about what I can do, try asking me for help.',
        'My source code is available at https://github.com/jakebasile/yaubot',
    ]
