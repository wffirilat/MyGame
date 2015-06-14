from ModLoader import Mod

__author__ = 'xwffirilat'

from event.Events import EventHandler
from event.EventLib import MonsterEvent

import MainRegistry


@Mod(modid='MonsterInformer')
class MonsterInformer:
    @staticmethod
    @EventHandler()
    def preAlert(event: MonsterEvent.Pre):
        MainRegistry.getGUI().console.add("creating Monster:\n"
                                          "    Size: {}\n    Type: {}\n    Name: {}"
                                          .format(event.size, event.type, event.name))

    @staticmethod
    @EventHandler()
    def postAlert(event: MonsterEvent.Post):
        MainRegistry.getGUI().console.add("Finished monster:\n"
                                          "    Level: {}\n    HP: {}"
                                          .format(event.monster.level, event.monster.health))
