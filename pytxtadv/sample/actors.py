from pytxtadv import actors

class Ace(actors.Player):
    def __init__(self):
        name = "Ace"
        description = "You are a dude trying to save the world"
        super().__init__(name,description)