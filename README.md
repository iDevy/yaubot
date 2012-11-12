# Yaubot

Frustrated with Hubot being terrible to install? Try **Yet Another Unnecessary Bot**!

## Installation

    $ pip install yaubot

That's it. Move on to the next section.

## Scripts

### Premade Scripts

Yaubot works with `pip` to manage its scripts. There are several packages available written by me, and feel free to write your own. You install them the same as anything else with `pip`:

    $ pip install yaubot-fun-scripts

**IMPORTANT**: You must be in the same virtualenv that yaubot was installed in!

**NOTE**: Yaubot must be restarted to recognize new scripts.

### Custom Scripts

To make your own scripts, put them in a package structure like this:

    my-custom-yaubot-scripts/
        setup.py
        yaubot/
            __init__.py
            scripts/
                __init__.py
                mycustomscripts/
                    __init__.py
                    foo.py
                    bar.py

It will need a minimal `setup.py` that declares any requirements. Here is some boilerplate:

    from setuptools import setup, find_packages

    setup(
        name='my-custom-yaubot-scripts',
        version='0.1',
        description='super awesome custom scripts!',
        author='John Q Taxpayer',
        packages=find_packages(),
        install_requires=[
            'yaubot==0.1',
        ],
    )

You would then install them with pip:

    $ pip install /path/to/my-custom-yaubot-scripts

Do not use `pip -e` while working on scripts! The entire yaubot package must be uninstalled and reinstalled:

    $ pip freeze | grep yaubot | sed 's/\(.*\)==.*/\1/' | xargs pip uninstall -y
    $ pip install yaubot /path/to/my-custom-yaubot-scripts

I know this is less than ideal. I'm working on making it better.

## Configuration

Currently Yaubot only supports IRC. To set that up:

    $ export YAUBOT_IRC_SERV=irc.derpnet.org \
        YAUBOT_IRC_PORT=6667 \
        YAUBOT_IRC_CHANS='#derp,#derp2' \
        YAUBOT_NAME='jarvis'
    $ yaubot-runner irc

And it's running.

