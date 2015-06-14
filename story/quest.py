__author__ = 'xwffirilat'


class Quest:
    def __init__(self, description, location, goal, reward=None):
        self.description = description
        self.location = location
        self.goal = goal
        self.reward = reward

    def proposeQuest(self, player):
        print(self.description)
        b = None
        while b is None:
            b = input('Would you like to accept the quest? ')
            if b.startswith('y'):
                b = True
            elif b.startswith('n'):
                b = False
            else:
                b = None
        if not b:
            return
        player.quests.append(self)

    def completeQuest(self, player):
        print('You have completed the quest!')
        player.quests.remove(self)
        player.inventory.extend(self.reward)
