__author__ = 'xwffirilat'

from command.registry import CommandRegistry


class Command:
    def __init__(self, name, func=lambda self, *args: None):
        self.name = name
        self._func = func
        self.__doc__ = func.__doc__
        CommandRegistry[self.name] = self

    def __call__(self, *args):
        return self._func(*args)


class Prompt:
    def __init__(self, prompt, player):
        self.player = player
        self.player.GUI.console.add(prompt + '\n')
