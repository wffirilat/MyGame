from entity.entity import Entity
from event.EventLib import ExperienceEvent, MonsterEvent
from event.Events import post

__author__ = 'xwffirilat'


class Monster(Entity):
    def __init__(self, size, type, name='Monster'):

        event = MonsterEvent.Pre(size, type, name)
        post(event)
        size, type, name = event.size, event.type, event.name

        super().__init__(name)

        self.size = size
        self.type = type

        self._maxHealth += self.size.hp
        self._damage += self.size.dmg
        self._armor += self.size.armor
        self._stealth += self.size.stealth
        self.level = self.size.level

        self._maxHealth += self.type.hp * self.level
        self._armor += self.type.armor * self.level
        self._damage += self.type.dmg * self.level
        self._stealth += self.type.stealth * self.level

        self.description = self.size.desc.format(self.name)

        self.fullHeal()

        self.givesxp = True
        self.experience = self.level

        event = MonsterEvent.Post(self)
        post(event)

    def getExperience(self, player):
        event = ExperienceEvent(self, player)
        post(event)
        return event.experience
