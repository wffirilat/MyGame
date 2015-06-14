from ModLoader import Mod, ModManager

__author__ = 'xwffirilat'

from event.Events import EventHandler
from event.EventLib import EntityAttackedEvent, EntityAttackEvent

import MainRegistry


@EventHandler()
def alertAttack(event: EntityAttackedEvent):
    MainRegistry.getGUI().console.add('%s was attacked by %s for %s damage' %
                                      (event.target, event.source, event.damage))


@EventHandler()
def alertSwing(event: EntityAttackEvent):
    MainRegistry.getGUI().console.add('%s (%s) swings at %s (%s)!' %
                                      (event.attacker, event.atkRoll, event.target, event.defRoll))


@Mod(modid='CombatAnnouncer')
class CombatAnnouncer(ModManager):
    alertAttack = alertAttack
    alertSwing = alertSwing

    @staticmethod
    def load():
        pass

    @staticmethod
    def disable():
        alertAttack.disable()
        alertSwing.disable()

    @staticmethod
    def reenable():
        alertAttack.reenable()
        alertSwing.reenable()
