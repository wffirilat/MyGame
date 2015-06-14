__author__ = 'xwffirilat'

_player = None
_GUI = None
_interpreter = None


def getInterpreter():
    return _interpreter


def getPlayer():
    return _player


def getGUI():
    return _GUI


def getGameVersion():
    return 0.1


def setPlayer(player):
    global _player
    _player = player


def setInterpreter(interpreter):
    global _interpreter
    _interpreter = interpreter


def setGUI(GUI):
    global _GUI
    _GUI = GUI
