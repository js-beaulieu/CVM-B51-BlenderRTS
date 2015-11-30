import bge
from mouse import *
from keyboard import *
from building import *
from civilisation import *
from ressource import *
import random



class Game():

    def __init__(self, players):
        """param: self, number of players"""
        self.players = players
        self.civilisations = []
        self.ressources = []
        self.buildings = []
        self.units = []
        self.dead_units = []
        self.selected_units = []
        self.bullets = []
        self.seed = 7
        random.seed(self.seed)

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        for i in range(self.players):
            self.civilisation = Civilisation(i)
            self.civilisations.append(self.civilisation)
        for civ in self.civilisations:
            civ.civ_init()
        self.ressources.append(Mine(scene.addObject('Mine', scene.objects['SpawnM'])))
        self.ressources.append(Crystal(scene.addObject('Crystal', scene.objects['SpawnC'])))
        tree_rotation = 0
        for i in range(15):
            # rangex =
            posX = random.randint(-11, 8)
            posY = random.randint(3, 25)
            scene.objects['SpawnT'].worldPosition[0] = posX
            scene.objects['SpawnT'].worldPosition[1] = posY
            new_tree = Tree(scene.addObject('Tree', scene.objects['SpawnT']))
            rotation = random.randint(0, 5)
            new_tree.applyRotation([0, 0, rotation], False)
            self.ressources.append(new_tree)




    def game_update(self):
        if len(self.bullets) > 0:
            for obj in self.bullets:
                obj.trajectory(obj.worldPosition[0], obj.worldPosition[1])
        for civ in self.civilisations:
            civ.civ_update()



