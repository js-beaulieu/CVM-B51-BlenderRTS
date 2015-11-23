import bge
from mouse import *
from keyboard import *
from building import *
from civilisation import *
from mine import *


class Game():

    def __init__(self, players):
        """param: self, number of players"""
        self.players = players
        self.civilisations = []
        self.mines = []
        self.buildings = []
        self.units = []
        self.dead_units = []
        self.selected_units = []
        self.bullets = []

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        for i in range(self.players):
            self.civilisation = Civilisation(i)
            self.civilisations.append(self.civilisation)
            self.civilisation.civ_init()
        Mine(scene.addObject('Mine', scene.objects['SpawnM']))

    def game_update(self):
        if len(self.bullets) > 0:
            for obj in self.bullets:
                obj.trajectory(obj.worldPosition[0], obj.worldPosition[1])
        for civ in self.civilisations:
            for obj in civ.units:
                obj.act()



