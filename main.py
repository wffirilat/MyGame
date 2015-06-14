#!/usr/bin/env python3

from entity.monster import Monster
from game import Game
import command.commands
from story.Class import Classes
from story.location import Location
from entity.monsterSize import Sizes
from entity.monsterType import Types
from story.locationregistry import LocationRegistry

__author__ = 'xwffirilat'

command.commands.init()


def loadMods():
    import ModLoader

    return ModLoader


def initLocations():
    Location('Cave')
    Location('Hamlet Shop')


def main():
    loadMods()

    game = Game()

    game.player.setClass(Classes.S3Cr37)
    game.player.name = 'Moo'

    initLocations()

    m = Monster(Sizes.Small, Types.Beast)
    LocationRegistry['Cave'].addNpcs(m)

    game.player.location = LocationRegistry['Cave']
    game.player.attack(LocationRegistry['Cave'].npcs['Monster'])

    game.gui.mainloop()


if __name__ == '__main__':
    main()
