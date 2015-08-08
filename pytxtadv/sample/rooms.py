from pytxtadv import rooms
from pytxtadv.game import end_game
        
class Corridor(rooms.Room):
    def __init__(self):
        name = "Dark Corridor"
        description = "Shadows flicker along the dark surface of the corridor"

        super().__init__(name, description)
        self.show_exits = True

class Hall(rooms.Room):
    def __init__(self):
        name = "Hall"
        description = "Multiple corridors connect to the giant hall"

        super().__init__(name, description)
        self.show_exits = True

class Center(rooms.Room):
    def __init__(self):
        name = "Heart of the Labyrinth"
        description = "A giant crystal floats in the air"

        super().__init__(name,description)
        
    def enter(self,actor,direction):
        print("You found the Heart of the Labyrinth!")
        print("YOU WIN!")
        end_game()
        
def build_rooms():
    start = Corridor()
    room_1 = Corridor()
    room_2 = Corridor()
    room_3 = Corridor()
    room_4 = Corridor()
    room_5 = Corridor()
    room_6 = Corridor()
    room_7 = Corridor()
    room_8 = Corridor()
    room_9 = Hall()
    room_10 = Corridor()
    room_11 = Hall()
    room_12 = Corridor()
    room_13 = Corridor()
    room_14 = Corridor()
    room_15 = Corridor()
    room_16 = Corridor()
    room_17 = Corridor()
    room_18 = Corridor()
    room_19 = Corridor()
    room_20 = Hall()
    room_21 = Corridor()
    room_22 = Corridor()
    room_23 = Corridor()
    end = Center()
    
    rooms.connect(start,'north',room_1)
    rooms.connect(room_1,'north',room_2)
    rooms.connect(room_2,'north',room_3)
    rooms.connect(room_3,'north',room_4)
    rooms.connect(start,'east',room_5)
    rooms.connect(room_5,'east',room_6)
    rooms.connect(room_6,'north',room_7)
    rooms.connect(room_7,'east',room_8)
    rooms.connect(room_8,'north',room_9)
    rooms.connect(room_9,'west',end)
    rooms.connect(room_9,'north',room_10)
    rooms.connect(room_10,'west',room_11)
    rooms.connect(room_11,'north',room_12)
    rooms.connect(room_12,'east',room_13)
    rooms.connect(room_13,'east',room_14)
    rooms.connect(room_14,'south',room_15)
    rooms.connect(room_15,'south',room_16)
    rooms.connect(room_16,'south',room_17)
    rooms.connect(room_17,'south',room_18)
    rooms.connect(room_18,'west',room_19)
    rooms.connect(room_11,'west',room_20)
    rooms.connect(room_20,'north',room_21)
    rooms.connect(room_20,'south',room_22)
    rooms.connect(room_22,'south',room_23)
    

    return start
