import sys

from command.command import Command
import MainRegistry
from command.registry import CommandRegistry
from internal.exception import CommandException
from story.locationregistry import LocationRegistry

__author__ = 'xwffirilat'


def _playerGoto(name):
    """goto <location>
    send the player to the location"""
    p = MainRegistry.getPlayer()
    l = LocationRegistry.get(name, None)
    if l is None:
        return 'Location not found: "{}"'.format(name)
    p.location = l
    return '%s travels to %s' % (p, name)


def _playerAttack(target):
    player = MainRegistry.getPlayer()
    _tname = target
    target = player.location.npcs.get(target, None)
    if target is None:
        return 'Target "%s" not found' % _tname
    player.attack(target)


def _help(command):
    return CommandRegistry[command].__doc__



def init():
    Command('help', _help)
    Command('?', _help)
    Command('echo', lambda *args: ' '.join(args))
    Command('quit', sys.exit)
    Command('attack', _playerAttack)
    Command('goto', _playerGoto)
    Command('>>>', lambda *args: exec(' '.join(args)))
