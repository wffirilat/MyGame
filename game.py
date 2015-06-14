from UI.GUI import GUI
from entity.player import Player
from event.EventLib import GameEvent
from event.Events import post
from story.location import Location

__author__ = 'xwffirilat'


class Game:
    def __init__(self):
        self.player = Player()
        self.gui = GUI()

        event = GameEvent.PreInit(self.player, self.gui)
        post(event)
        self.player, self.gui = event.player, event.GUI

        Hamlet = Location('Hamlet')
        self.player.init(self.gui, Hamlet)
        self.gui.init(self.player)

        event = GameEvent.PostInit(self)
        post(event)
