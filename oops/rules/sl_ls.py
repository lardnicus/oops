"""
This happens way too often

When typing really fast cause I'm a 1337 H4X0R,
I often stuff up 'ls' and type 'sl'. No more!
"""


def match(command, settings):
    return command.script == 'sl'


def get_new_command(command, settings):
    return 'ls'
