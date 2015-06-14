from story.locationregistry import LocationRegistry

__author__ = 'xwffirilat'


class Location:
    def __init__(self, name: str, *npcs):
        LocationRegistry[name] = self
        self.name = name
        self.npcs = {npc.name: npc for npc in npcs}

    def addNpcs(self, *npcs):
        for npc in npcs:
            self.npcs[npc.name] = npc
