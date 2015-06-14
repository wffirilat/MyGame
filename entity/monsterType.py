from enum import Enum

__author__ = 'xwffirilat'


class Type:
    def __init__(self, hp, dmg, armor, stealth):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.stealth = stealth


class Types(Enum):
    Brute = Type(hp=0, dmg=0, armor=2, stealth=0)
    Beast = Type(hp=5, dmg=0, armor=0, stealth=0)
    Slime = Type(hp=0, dmg=0, armor=0, stealth=2)
    Fiend = Type(hp=0, dmg=2, armor=0, stealth=0)
