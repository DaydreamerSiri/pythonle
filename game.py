from uhrzeit import time
from creatures import Creatures
import world

class Game(object):
    """dauerhaftes Input fuer das spiel"""
    def __init__(self):
        self.listcreatures = Creatures()
    def startgame(self):
        "Input Game #1"
        a = 0
        rawq = raw_input("\nhi")
        if rawq == "hi" or rawq == "hallo":
            rawq = raw_input("\nwie geht es ihnen?")
            if rawq == "gut":
                print("\ngleich aber nicht mehr")
                while True:
                    time.sleep(1)
                    a += 1
                    print("Loading")
                    if a == 10:
                        a = 0
                        break 
                    rawq = raw_input("\nselbstzerstoerungseinheit wird "
                    "aktiviert zum abbrechen bitte die 1 druecken")
                    while True:
                        a += 1
                        time.sleep(1.1)
                        print(a)
                        if a == 10:
                            print("sie haben verloren programm schliesst "
                            "sich in 10 sekunden")
                            time.sleep(10)
                            quit()
                        elif rawq == "1":
                            print("\nhmm sie haben doch noch glueck gehabt"
                            "!")
                            break
                            self.world1()
        return
    
    def world1(self):
        a = 0
        while True:
            a += 1
            print("\nLade Welt bitte warten...")
            if a == 10:
                break
        self.listcreatures.player(100, 60, 20)
        print("\nDu siehst einen Pfad voraus")
        print("\nwas willst du tun?")
        print("moegliche Optionen:" 
        "\nEquip,Move,Leave")
        rawq = raw_input("")
        if rawq == "move":
            print("\n moegliche Optionen:\n forward, back,")