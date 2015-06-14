import MainRegistry

__author__ = 'xwffirilat'

import Mods


class Mod:
    def __init__(self, modid, version=1.0, gameversion=MainRegistry.getGameVersion()):
        self.modid = modid
        self.version = version
        self.gameversion = gameversion

    def __call__(self, cls):
        cls.version = self.version
        cls.gameVersion = self.gameversion
        setattr(Mods, self.modid, cls)
