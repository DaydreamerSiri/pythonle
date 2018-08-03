from uhrzeit import time
from creatures import Creatures
import random
import world
class Game(object):
    """dauerhaftes Input fuer das spiel"""
    def __init__(self):
        self.listcreatures = Creatures()
        self.rand = random
        self.check = True
    def startgame(self):
        while True:
            "Input Game #1"
            self.a = 0
            rawq = raw_input("\nhi")
            if rawq == "hi" or rawq == "hallo":
                rawq = raw_input("\nwie geht es ihnen?")
                if rawq == "gut":
                    print("\ngleich aber nicht mehr")
                    while self.check == True:
                        time.sleep(1)
                        self.a += 1
                        print("Loading") 
                        if self.a == 10:
                            self.check = False
                    else:
                        b = 0
                        rawq = raw_input("\nselbstzerstoerungseinheit wird"
                        "aktiviert zum abbrechen bitte die 1 druecken")
                        while True:
                            if b == 10:
                                print("sie haben verloren programm schliesst "
                                "sich in 10 sekunden")
                                time.sleep(10)
                                quit()
                            if rawq == "1":
                                print("\nhmm sie haben doch noch glueck gehabt"
                                "!")
                                self.world1()
                            b += 1
                            time.sleep(1.1)
                            print(b)
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
        player = self.listcreatures.Player()
        player.player()
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
                
                
            