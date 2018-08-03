#creatures.py
class Creatures(object):
    """Liste von Kreaturen"""
    class Player(object):
        """Spieler Class"""
        def __init__(self):
            self.phealth = 0
            self.damage = 0
            self.armor = 0
            self.diffc = 0
        def player(self, phealth= 0 , armor= 0 , damage= 0):
            if self.diffc == 1:
                self.phealth = phealth
                self.armor = armor
                self.damage = damage
            elif self.diffc == 2:
                self.phealth = phealth - 15
                self.armor = armor - 5
                self.damage = damage - 10
            elif self.diffc == 3:
                self.phealth = phealth - 50
                self.armor = armor - 25
                self.damage = damage - 15
    class Npcs(object):
        """Liste der Nicht Spielbaren Charaktere"""
        class Enemys(object):
            def __init__(self):
                self.health = 0
                self.damage = 0
                self.armor = 0
                self.diffc = 0
            def goblin(self):
                self.health = 100
                self.damage = 10
                self.armor = 10