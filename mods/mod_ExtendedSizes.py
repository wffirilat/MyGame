__author__ = 'xwffirilat'

from entity.monsterSize import Size
from ModLoader import Mod, ModManager

Micro = Size(hp=5, dmg=1, armor=5, stealth=10, level=1, desc='A Minuscule {}')
Tiny = Size(hp=10, dmg=2, armor=3, stealth=7, level=1, desc='A {} smaller than a cat')
Colossal = Size(hp=150, dmg=20, armor=20, stealth=-1, level=7, desc='A mind-blowingly huge {}')


@Mod(modid='ExtendedSizes')
class ExtendedSizes(ModManager):
    Micro = Micro
    Tiny = Tiny
    Colossal = Colossal

    @staticmethod
    def load():
        pass

    @staticmethod
    def disable():
        pass

    @staticmethod
    def reenable():
        pass
