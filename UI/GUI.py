from tkinter import *
import MainRegistry

from UI.LabelEntry import LabelEntry
from UI.console import Console
from UI.equipment import EquipmentView
from UI.input import Input
from command.interpreter import Interpreter

__author__ = 'xwffirilat'


class GUI(Tk):
    # noinspection PyAttributeOutsideInit
    def init(self, player):
        MainRegistry.setGUI(self)
        self.player = player
        self.promptCallback = None
        self.currentInput = None
        self.info = Toplevel(self)
        self.title("Console")
        self.info.title("Player Info")
        self.info.protocol('WM_DELETE_WINDOW', lambda: None)
        self.loc = LabelEntry(self.info, 'Location: ', self.player.location.name)
        self.loc.grid(row=0, column=0)
        self.inv = EquipmentView(self.info, self.player)
        self.inv.grid(row=1, column=0)
        self.console = Console(self, height=9)
        self.console.grid(row=2, column=0, columnspan=3)
        self.input = Input(self, Interpreter(self), self.console, width=70)
        self.input.grid(row=3, column=0, columnspan=3)

    def update(self):
        self.inv.update()
        self.loc.updateText(self.player.location.name)
        super().update()
