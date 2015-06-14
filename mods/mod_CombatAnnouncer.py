__author__ = 'xwffirilat'

from event.Events import EventHandler, Priority
from event.EventLib import EntityAttackedEvent, EntityAttackEvent

import MainRegistry


@EventHandler(EntityAttackedEvent, priority=Priority.NORMAL)
def alertAttack(event: EntityAttackedEvent):
    MainRegistry.getGUI().console.add('%s was attacked by %s for %s damage' %
                                      (event.target, event.source, event.damage))


@EventHandler(EntityAttackEvent)
def alertSwing(event: EntityAttackEvent):
    MainRegistry.getGUI().console.add('%s (%s) swings at %s (%s)!' %
                                      (event.attacker, event.atkRoll, event.target, event.defRoll))
