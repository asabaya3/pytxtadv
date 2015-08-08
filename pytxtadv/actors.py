class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.aliases = []

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Actor):
            return super().__eq__(self, other)
        else:
            return any([other in name for name in self.aliases + [self.name]])

    def talk(self):
        print(self.name + " has nothing to say")

    def examine(self):
        print(self.description)
        
    def act(self):
        pass
        
    def update(self):
        pass

class Player(Actor):
    def __init__(self, name, description):
        super().__init__(name,description)
        self.inventory = []
        self.aliases = ["me", "myself", "I"]
        self.location = None

    def check_inventory(self, item_name):
        for item in self.inventory:
            if item == item_name:
                return item.get(item_name)
        return None