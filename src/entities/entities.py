# creates Entity class that's the base for all player/npcs and is just there in case some fundamentals might change
class Entity:
    def __init__(self, name, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.inventory = inventory
