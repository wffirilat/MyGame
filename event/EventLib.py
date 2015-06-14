__author__ = 'wffirilat'

from event.Events import Event


class EntityAttackedEvent(Event):
    def __init__(self, source, target, damage):
        super().__init__()
        self.source = source
        self.target = target
        self.damage = damage


class EntityAttackEvent(Event):
    def __init__(self, attacker, target, atkRoll, defRoll):
        super().__init__()
        self.attacker = attacker
        self.target = target
        self.atkRoll = atkRoll
        self.defRoll = defRoll


class ExperienceEvent(Event):
    def __init__(self, monster, player):
        super().__init__()
        self.experience = monster.experience
        self.monster = monster
        self.player = player


class MonsterEvent:
    class Pre(Event):
        def __init__(self, size, type, name):
            super().__init__()
            self.size = size
            self.type = type
            self.name = name

    class Post(Event):
        def __init__(self, monster):
            super().__init__()
            self.monster = monster


class PlayerEvent(Event):
    def __init__(self, player):
        super().__init__()
        self.player = player

    class PreInit(Event):
        def __init__(self, player):
            super().__init__()
            self.player = player

    class PostInit(Event):
        pass

    class LevelUp(Event):
        def __init__(self, player, levels):
            super().__init__()
            self.player = player
            self.levels = levels


class GameEvent:
    class PreInit(Event):
        def __init__(self, player, GUI):
            super().__init__()
            self.player = player
            self.GUI = GUI

    class PostInit(Event):
        def __init__(self, game):
            super().__init__()
            self.game = game
