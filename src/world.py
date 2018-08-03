#world.py
class World(object):
    """Welt Liste"""
    class Environment(object):
        """Die Umgebung"""
        def obstacle(self, damage= False, blocked= False,__null= False):
            """Hindernisse"""
            self.damage = damage
            self.blocked = blocked
            self.__null = __null
        def Roads(self,movementspeed= 0, roadtype= "-",__null= False):
            """Rennweg / Wege"""
            self.movementspeed = movementspeed
            self.roadtype = roadtype
            self.__null = __null
        def Buildings(self,passable= False, destroyed= False, __null= False):
            """Gebaeude"""
            self.passable = passable
            self.destroyed = destroyed
            self.__null = __null
    class RPG(object):
        """Rollenspiele Elemente"""
        def Quests(self,version= "",reward= 0, npc= ""):
            """Missionen"""
            self.type = version
            self.reward = reward
            self.npc = npc
        