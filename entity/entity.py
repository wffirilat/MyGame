import random
import MainRegistry

__author__ = 'xwffirilat'

from event.Events import post
from event.EventLib import EntityAttackedEvent, EntityAttackEvent


class Entity:
    def __init__(self, name='Entity'):
        self.name = name
        self.level = 1
        self.dead = False
        self.givesxp = False
        self._maxHealth = 0
        self._health = 0
        self._armor = 0
        self._damage = 0
        self._DR = 0
        self._search = 0
        self._stealth = 0
        self.proficient_armor = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health < 0:
            self.dead = True
            MainRegistry.getGUI().console.add('%s dies' % self)
        if self._health > self._maxHealth:
            self._health = self._maxHealth

    def fullHeal(self):
        self._health = self._maxHealth

    def onAttack(self, source, damage):
        event = EntityAttackedEvent(source, self, damage)
        post(event)
        damage = event.damage
        if not event.canceled:
            self.health -= damage

    def attack(self, target):
        if not self.canAct:
            MainRegistry.getGUI().console.add('%s tries to attack but can\'t' % self)
            return
        atkRoll = random.randint(0, self.damage)
        defRoll = random.randint(0, target.armor)
        event = EntityAttackEvent(self, target, atkRoll, defRoll)
        post(event)
        atkRoll, defRoll = event.atkRoll, event.defRoll
        if atkRoll > defRoll:
            target.onAttack(self, random.randint(1, self.damage))

    @property
    def canAct(self):
        return not self.dead

    @property
    def damage(self):
        return self._damage

    @property
    def armor(self):
        return self._armor

    @property
    def DR(self):
        return self._DR

    @property
    def search(self):
        return self._search

    @property
    def stealth(self):
        return self._stealth

    def __str__(self):
        return self.name
