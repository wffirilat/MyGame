__author__ = 'xwffirilat'
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, name='Item'):
        self.name = name
        self.slot = None

    @abstractmethod
    def equip(self, player):
        pass

    @abstractmethod
    def remove(self, player):
        pass

    def __str__(self):
        return self.name


class ArmorType:
    Leather = 0
    Chain = 1
    Plate = 2
    RuneCrest = 3


class WeaponType:
    Wand = 0
    Dagger = 1
    Sword = 2
    RuneBlade = 3


class InventorySlot:
    Armor = 'armor'
    Weapon = 'weapon'
    Trinket = 'trinket'


class Armor(Item):
    def __init__(self, defence, typ=ArmorType.Leather, name='Armor'):
        super().__init__(name)
        self.slot = InventorySlot.Armor
        self.type = typ
        self.defence = defence

    def equip(self, player):
        if player.proficient_armor >= self.type:
            player.addArmor(self.defence)
            return True
        print('Player {} cannot equip the {}!'.format(player.name, self.name))
        return False

    def remove(self, player):
        player.addArmor(-self.defence)


class Weapon(Item):
    def __init__(self, attack, typ=WeaponType.Wand, name='Weapon'):
        super().__init__(name)
        self.slot = InventorySlot.Weapon
        self.type = typ
        self.attack = attack

    def equip(self, player):
        if player.proficient_weapon >= self.type:
            player.addDamage(self.attack)
            return True
        print('Player {} cannot equip the {}!'.format(player.name, self.name))
        return False

    def remove(self, player):
        player.addDamage(-self.attack)


class Trinket(Item):
    def __init__(self, name='Trinket'):
        super().__init__(name)
        self.slot = InventorySlot.Trinket

    def equip(self, player):
        pass

    def remove(self, player):
        pass


class StealthTrinket(Trinket):
    def __init__(self, mod, name='Trinket'):
        super().__init__(name)
        self.stealth = mod

    def equip(self, player):
        player.addStealth(self.stealth)
        return True

    def remove(self, player):
        player.addStealth(-self.stealth)


class SearchTrinket(Trinket):
    def __init__(self, mod, name='Trinket'):
        super().__init__(name)
        self.search = mod

    def equip(self, player):
        player.addSearch(self.search)
        return True

    def remove(self, player):
        player.addSearch(-self.search)


class DRTrinket(Trinket):
    def __init__(self, mod, name='Trinket'):
        super().__init__(name)
        self.DR = mod

    def equip(self, player):
        player.addDR(self.DR)
        return True

    def remove(self, player):
        player.addDR(-self.DR)
