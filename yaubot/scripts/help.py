__matcher__ = '%NICK.*help'

def respond(brain, user, message, groups):
    yield 'name:\t|\tactivation regex\t|\tdescription'
    for script in brain.bot_info['scripts']:
        name = script.__name__.split('.')[-1]
        regex = script.__matcher__.replace('%NICK', brain.bot_info['nick'])
        doc = script.__doc__ if script.__doc__ is not None else ''
        yield '%s:\t|\t%s\t|\t%s' % (name, regex, doc)

