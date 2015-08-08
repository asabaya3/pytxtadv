from . import actors,rooms
from pytxtadv.game import start_game

def run():
    intro = "You are picked up from the street and thrown randomly into a hole. When you wake up you see a note explaining that you should head to the center of the maze if you want to live"
    start_game(actors.Ace(),rooms.build_rooms(), intro)