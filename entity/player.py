import MainRegistry
from entity.playerInventory import Inventory
from entity.entity import Entity
from event.EventLib import PlayerEvent
from event.Events import post
from story.Class import Classes
from story import Class
from story.item import Item


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.cls = Classes.NONE
        self.name = ''
        self.level = 1
        self._experience = 0
        self.proficient_armor = 0

    # noinspection PyAttributeOutsideInit
    def init(self, GUI, location):
        MainRegistry.setPlayer(self)
        self.GUI = GUI
        self.items = Inventory(self)
        self.location = location
        self.locations = [location]
        self.quests = []
        self.inventory = []

    def chooseClass(self):
        choice = None
        while choice is None:
            choice = input('''Choose a class:
    Warrior: High health, moderate damage, high armor.
    Mage: Low health, very high damage, low armor.
    Rogue: Moderate health, high damage (sneak attack), moderate armor.

    -> ''')
            # noinspection PyProtectedMember
            if choice not in Classes._member_names_:
                choice = None
                print('Invalid class choice')
            else:
                choice = getattr(Classes, choice, None)
        self.setClass(choice)

    def chooseName(self):
        name = input('Choose a name -> ')
        self.name = name

    def attack(self, target):
        super().attack(target)
        if target.givesxp and target.dead:
            self.experience += target.getExperience(self)

    def setClass(self, cls: Class):
        self.cls = cls
        self._maxHealth = cls.health
        self._health = self._maxHealth
        self._armor = cls.armor
        self._damage = cls.damage
        self.proficient_armor = cls.proficient_armor

    def addItem(self, item: Item):
        if item.equip(self):
            self.items.add(item)
            return True
        return False

    def removeItem(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            item.remove(self)

    def addArmor(self, defence):
        self._armor += defence

    def addDamage(self, damage):
        self._damage += damage

    def addDR(self, DR):
        self._DR += DR

    def addSearch(self, search):
        self._search += search

    def addStealth(self, stealth):
        self._stealth += stealth

    def levelUp(self, levels=1):

        event = PlayerEvent.LevelUp(self, levels)
        post(event)
        levels = event.levels

        log = MainRegistry.getGUI().console

        log.indent('|')

        log.add('==+==+==+==+==+==+==+==+==+==+==+==+==+==+==+==+==')

        log.add('%s has increased to level %s!' % (self, self.level))

        log.indent(' *  ')

        self._maxHealth += levels * self.cls.hpperlvl
        log.add('%s\'s health increased by %s' % (self, levels * self.cls.hpperlvl))

        self.fullHeal()

        self.addArmor(levels * self.cls.armorperlvl)
        log.add('%s\'s armor increased by %s' % (self, levels * self.cls.armorperlvl))

        self.addArmor(levels * self.cls.damageperlvl)
        log.add('%s\'s damage increased by %s' % (self, levels * self.cls.damageperlvl))

        self.addDR(levels * self.cls.drperlvl)

        self.addSearch(levels * self.cls.searchperlvl)
        log.add('%s\'s search increased by %s' % (self, levels * self.cls.searchperlvl))

        self.addStealth(levels * self.cls.stealthperlvl)
        log.add('%s\'s stealth increased by %s' % (self, levels * self.cls.stealthperlvl))

        log.dedent()

        log.add('==+==+==+==+==+==+==+==+==+==+==+==+==+==+==+==+==')

        log.dedent()

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new):
        self._experience = new
        if self._experience >= self.level ** 2:
            self._experience -= self.level ** 2
            self.level += 1
            self.levelUp(1)
