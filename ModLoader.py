import MainRegistry

__author__ = 'xwffirilat'

import Mods


def Mod(modid, version=1.0, gameversion=MainRegistry.getGameVersion()):
    def deco(cls):
        cls.version = version
        cls.gameVersion = gameversion
        setattr(Mods, modid, cls)

    return deco
