from ModLoader import Mod, ModManager

__author__ = 'xwffirilat'

from event.Events import EventHandler
from event.EventLib import MonsterEvent

import MainRegistry


@EventHandler()
def preAlert(event: MonsterEvent.Pre):
    MainRegistry.getGUI().console.add("creating Monster:\n"
                                      "    Size: {}\n    Type: {}\n    Name: {}"
                                      .format(event.size, event.type, event.name))


@EventHandler()
def postAlert(event: MonsterEvent.Post):
    MainRegistry.getGUI().console.add("Finished monster:\n"
                                      "    Level: {}\n    HP: {}"
                                      .format(event.monster.level, event.monster.health))


@Mod(modid='MonsterInformer')
class MonsterInformer(ModManager):
    preAlert = preAlert
    postAlert = postAlert

    @staticmethod
    def load():
        pass

    @staticmethod
    def disable():
        preAlert.disable()
        postAlert.disable()

    @staticmethod
    def reenable():
        preAlert.reenable()
        postAlert.reenable()
