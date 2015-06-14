from tkinter import Frame

from UI.LabelEntry import LabelEntry

__author__ = 'xwffirilat'


class EquipmentView(Frame):
    # noinspection PyDefaultArgument
    def __init__(self, tk, player, cnf={}, **kwargs):
        super().__init__(tk, cnf, **kwargs)
        self.player = player
        self.armor = LabelEntry(self, 'Armor: ', self.player.items.armor.name)
        self.armor.grid(row=0, column=0)
        self.weapon = LabelEntry(self, 'Weapon: ', self.player.items.weapon.name)
        self.weapon.grid(row=1, column=0)
        self.trinket = LabelEntry(self, 'Trinket: ', self.player.items.trinket.name)
        self.trinket.grid(row=2, column=0)

    def update(self):
        self.armor.updateText(self.player.items.armor.name)
        self.weapon.updateText(self.player.items.weapon.name)
        self.trinket.updateText(self.player.items.trinket.name)
        super().update()
