__author__ = 'xwffirilat'

from entity.monsterSize import Sizes, Size
from ModLoader import Mod


@Mod(modid='ExtendedSizes')
class ExtendedSizes:
    Micro = Size(hp=5, dmg=1, armor=5, stealth=10, level=1, desc='A Miniscule {}')
    Tiny = Size(hp=10, dmg=2, armor=3, stealth=7, level=1, desc='A {} smaller than a cat')

    Colossal = Size(hp=150, dmg=20, armor=20, stealth=-1, level=7, desc='A mind-blowingly huge {}')
