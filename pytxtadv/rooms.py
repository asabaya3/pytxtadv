class Room:

    inverse_direction = {
        'north' : 'south',
        'south' : 'north',
        'east' : 'west',
        'west' : 'east',
        'up' : 'down',
        'down' : 'up',
        'in' : 'out',
        'out' : 'in',
        }

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.actors = []
        self.items = []
        self.exits = {}
        self.show_exits = False

    def __repr__(self):
        return self.name

    def examine(self):
        print(self.description)
        print("People: " + (str(self.actors)))
        print("Items: " + (str(self.items)))
        if self.show_exits:
            print("Exits: " + ','.join(self.exits.keys()))

    def enter(self, actor, direction = 'start'):
        print(actor.name + " enters " + self.name + " from the " + direction)
        self.actors.append(actor)
        self.examine()

    def exit(self, actor, direction):
        exit = self.exits.get(direction)
        if exit:
            self.actors.remove(actor)
            print(actor.name + " exits to the " + direction)
            return (exit, Room.inverse_direction[direction])
        else:
            print("There is no exit there")
            return (None, None)

    def take(self, item, target):
        if item.take(target):
            self.items.remove(item)

    def drop(self, item, target):
        if item.drop(target):
            self.items.append(item)

    def check_actors(self, actor_name):
        for actor in self.actors:
            if actor == actor_name:
                return actor
        return None
        
    def check_items(self, item_name):
        for item in self.items:
            if item == item_name:
                return item.get(item_name)
        return None

    def check_room(self, room_name):
        return room_name in self.name

def connect(room_a, direction, room_b):
    inv_direc = Room.inverse_direction[direction]
    room_a.exits[direction] = room_b
    room_b.exits[inv_direc] = room_a
