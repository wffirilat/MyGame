from ModLoader import Mod

__author__ = 'xwffirilat'

from event.Events import EventHandler, Priority
from event.EventLib import EntityAttackedEvent, EntityAttackEvent

import MainRegistry


@Mod(modid='CombatAnnouncer')
class CombatAnnouncer:
    @staticmethod
    @EventHandler()
    def alertAttack(event: EntityAttackedEvent):
        MainRegistry.getGUI().console.add('%s was attacked by %s for %s damage' %
                                          (event.target, event.source, event.damage))

    @staticmethod
    @EventHandler()
    def alertSwing(event: EntityAttackEvent):
        MainRegistry.getGUI().console.add('%s (%s) swings at %s (%s)!' %
                                          (event.attacker, event.atkRoll, event.target, event.defRoll))
