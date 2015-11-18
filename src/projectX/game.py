import bge
from mouse import *
from keyboard import *
from building import *
from civilisation import *
from mine import *


class Game():

    def __init__(self):
        self.civilisations = []
        self.mines = []
        self.units = []
        self.dead_units = []
        self.selected_units = []
        self.bullets = []

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        self.civilisation = Civilisation()
        self.civilisations.append(self.civilisation)
        self.civilisation.civ_init()
        Mine(scene.addObject('Mine', scene.objects['SpawnM']))

    def game_update(self):
        if len(self.dead_units) > 0:
            for obj in self.dead_units:
                self.units.remove(obj)
                self.dead_units.remove(obj)
                obj.endObject()
            self.dead_units = []
        for obj in self.units:
            obj.act()
        if len(self.bullets) > 0:
            for obj in self.bullets:
                obj.trajectory(obj.worldPosition[0], obj.worldPosition[1])



