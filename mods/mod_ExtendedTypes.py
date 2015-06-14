from ModLoader import Mod

__author__ = 'xwffirilat'

from entity.monsterType import Types, Type


@Mod(modid='ExtendedTypes')
class ExtendedTypes:
    Vermin = Type(hp=0, dmg=0, armor=1, stealth=1)
    Type(hp=3, dmg=1, armor=0, stealth=0)
    Type(hp=3, dmg=0, armor=1, stealth=0)
    Type(hp=3, dmg=0, armor=0, stealth=1)
    Type(hp=0, dmg=1, armor=1, stealth=0)
    Type(hp=0, dmg=1, armor=0, stealth=1)

    Dragon = Type(hp=5, dmg=2, armor=2, stealth=0)
