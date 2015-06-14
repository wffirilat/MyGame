__author__ = 'xwffirilat'

import MainRegistry
from command.registry import CommandRegistry
from internal.exception import CommandException


class Interpreter:
    def __init__(self, GUI):
        MainRegistry.setInterpreter(self)
        self.GUI = GUI

    def interpret(self, string: str):
        command, *args = string.split(' ')
        try:
            cmd = CommandRegistry[command]
            r = cmd(*args)
            if r is None:
                return ''
            else:
                return r
        except CommandException as e:
            self.GUI.console.add(e.args[0])
            return ''
