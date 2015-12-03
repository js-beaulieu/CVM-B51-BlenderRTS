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
        self.ressources = {
            "mines": [],
            "veins": [],
            "trees": []
        }
        self.buildings = []
        self.selected_units = []
        self.bullets = []
        self.seed = 7
        random.seed(self.seed)

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        mines_loc = [[-8, -11, 1], [55, -11, 1]]
        for i in range(self.players):
            self.civilisation = Civilisation(i)
            self.civilisations.append(self.civilisation)
            scene.objects['SpawnM'].worldPosition = mines_loc[i]
            self.ressources["mines"].append(Mine(scene.addObject('Mine', scene.objects['SpawnM'])))
        for civ in self.civilisations:
            civ.civ_init()
        scene.objects['SpawnC'].worldPosition = [22, 13, 1]
        self.ressources["veins"].append(Crystal(scene.addObject('Crystal', scene.objects['SpawnC'])))
        for i in range(15):
            posX = random.randint(-10, 15)
            posY = random.randint(3, 30)
            scene.objects['SpawnT'].worldPosition[0] = posX
            scene.objects['SpawnT'].worldPosition[1] = posY
            new_tree = Tree(scene.addObject('Tree', scene.objects['SpawnT']))
            rotation = random.randint(0, 5)
            new_tree.applyRotation([0, 0, rotation], False)
            self.ressources["trees"].append(new_tree)
        for i in range(15):
            posX = random.randint(30, 55)
            posY = random.randint(3, 30)
            scene.objects['SpawnT'].worldPosition[0] = posX
            scene.objects['SpawnT'].worldPosition[1] = posY
            new_tree = Tree(scene.addObject('Tree', scene.objects['SpawnT']))
            rotation = random.randint(0, 5)
            new_tree.applyRotation([0, 0, rotation], False)
            self.ressources["trees"].append(new_tree)

    def game_update(self):
        if len(self.bullets) > 0:
            for obj in self.bullets:
                obj.trajectory(obj.worldPosition[0], obj.worldPosition[1])
        for civ in self.civilisations:
            civ.civ_update()

