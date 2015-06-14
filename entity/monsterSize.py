from enum import Enum

__author__ = 'xwffirilat'


class Size:
    def __init__(self, hp, dmg, armor, stealth, level, desc, dr=0):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.stealth = stealth
        self.level = level
        self.dr = dr
        self.desc = desc


class Sizes(Enum):
    Small = Size(20, 3, 3, 4, 1, '{} half your size')
    Medium = Size(30, 5, 5, 3, 2, '{} as large as you')
    Large = Size(50, 8, 8, 2, 3, '{} twice your height')
    Huge = Size(70, 10, 10, 1, 4, 'fearsomely sized {}', 1)
    Gargantuan = Size(100, 13, 12, 0, 5, '{} larger than a house', 2)
