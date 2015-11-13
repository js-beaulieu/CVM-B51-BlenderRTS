import bge
from mouse import *
from keyboard import *
from building import *
from civilisation import *
from mine import *


class Game():

    def __init__(self):
        self.civilisations = []
        self.units = []
        self.selected_units = []
        self.moving_units = []

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        self.civilisation = Civilisation()
        self.civilisations.append(self.civilisation)
        self.civilisation.civ_init()
        Mine(scene.addObject('Mine', scene.objects['SpawnM']))

    def game_update(self):
        if self.moving_units:
            for obj in self.moving_units:
                x = obj.worldPosition[0]
                y = obj.worldPosition[1]
                obj.move(x, y)
                if not obj.moving:
                    self.moving_units.remove(obj)


