from enum import Enum

__author__ = 'xwffirilat'


class Type:
    def __init__(self, hp, dmg, armor, stealth):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.stealth = stealth


class Types(Type, Enum):
    Brute = 0, 0, 2, 0
    Beast = 5, 0, 0, 0
    Slime = 0, 0, 0, 2
    Fiend = 0, 2, 0, 0
