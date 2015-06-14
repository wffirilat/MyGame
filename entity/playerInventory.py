from story.item import Armor, Weapon, Trinket, Item

__author__ = 'xwffirilat'


class Inventory(object):
    def __init__(self, player):
        self.player = player
        self.armor = Armor(0, name='None')
        self.weapon = Weapon(0, name='None')
        self.trinket = Trinket(name='None')

    def add(self, item: Item):
        slot = item.slot
        if getattr(self, slot):
            self.remove(getattr(self, slot))

    def remove(self, item: Item):
        slot = item.slot
        if getattr(self, slot):
            setattr(self, slot, None)
            self.player.inventory.add(item)
