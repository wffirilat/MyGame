__author__ = 'xwffirilat'

from enum import Enum


class Class:
    def __init__(self, health, damage, armor, hpperlvl, armorperlevel, damageperlevel, drperlevel, searchperlevel,
                 stealthperlevel):
        self.proficient_armor = (armor - 1) // 2
        self.health = health
        self.damage = damage
        self.armor = armor
        self.hpperlvl = hpperlvl
        self.armorperlvl = armorperlevel
        self.damageperlvl = damageperlevel
        self.drperlvl = drperlevel
        self.searchperlvl = searchperlevel
        self.stealthperlvl = stealthperlevel


class Classes(Class, Enum):
    NONE = 0, 0, 0, 0, 0, 0, 0, 0, 0
    S3Cr37 = 40, 20, 8, 6, 6, 6, 2, 6, 6
    Warrior = 30, 5, 5, 5, 3, 2, 0, 1, 1
    Mage = 10, 7, 2, 1, 1, 5, 0, 3, 2
    Rogue = 20, 3, 3, 2, 1, 1, 0, 3, 5
