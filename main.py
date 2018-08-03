#Main.py
from uhrzeit import Uhr
from game import Game
import threading
from threading import Thread

class Engine(object):
    """Fuert die Befehle aus"""
    def __init__(self):
        self.settings = threading.Thread
        self.zeit = Uhr()
        self.spiel = Game()
    def timer(self):
        """funktion fuer die uhr"""
        self.zeit.shitlisting()
    def game(self):
        """funktion fur das spiel"""
        self.spiel.startgame()
    def systhreads(self):
        """die prozesse fur das programm"""
        p1 = Thread(target=starting.timer)
        p2 = Thread(target=starting.game)
        p1.start()
        p2.start()
    def systhreadc(self):
        """beendet die prozesse"""
        Engine.systhreads.p1.join()
        Engine.systhreads.p2.join() 
        
"""startet das programm"""
if __name__ == "__main__":
    starting = Engine()
    starting.systhreads()