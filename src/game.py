from uhrzeit import time
from creatures import Creatures
import random
import world
class Game(object):
    """dauerhaftes Input fuer das spiel"""
    def __init__(self):
        self.listcreatures = Creatures()
        self.rand = random
    def startgame(self):
        while True:
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
                            b = 0
                            rawq = raw_input("\nselbstzerstoerungseinheit wird"
                            "aktiviert zum abbrechen bitte die 1 druecken")
                            while True:
                                b += 1
                                time.sleep(1.1)
                                print(b)
                                if b == 10:
                                    print("sie haben verloren programm schliesst "
                                    "sich in 10 sekunden")
                                    time.sleep(10)
                                    quit()
                            if rawq == "1":
                                print("\nhmm sie haben doch noch glueck gehabt"
                                "!")
                                self.world1()
            time.sleep(20)
        return
    def checkworld(self):
        self.builder = world.World()
        if self.builder.Environment.Buildings(False,True,False):
            print("Sie koennen nicht" + self.playerinput, "nutzen")
        else:
            print("Sie laufen" + self.playerinput)
        
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
        "\nEquip,Move,Leave,Inspect")
        rawq = raw_input("")
        if rawq == "move":
            print("\n moegliche Optionen:\n forward, back,left,right")
            self.playerinput = raw_input("")
            if self.playerinput == "forward":
                self.checkworld()
                
                
                
            