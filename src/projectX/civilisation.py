import bge
from building import *


class Civilisation():

    def __init__(self, id_nb):
        self.id_nb = id_nb
        self.buildings = []
        self.units = []
        self.gold = 1000
        self.computer = False

    def civ_init(self):
        scene = bge.logic.getCurrentScene()
        if self.id_nb == 0:
            self.buildings.append(self.create_building())
            self.buildings[0].color = [0, 1, 0, 1]
            for i in range(4):
                self.buildings[0].create_unit()
        if self.id_nb == 1:
            self.computer = True
            scene.objects['SpawnB'].worldPosition[0] = 4
            scene.objects['SpawnB'].worldPosition[1] = -15
            self.buildings.append(self.create_building())
            self.buildings[0].color = [1, 0, 0, 1]
            for i in range(4):
                self.buildings[0].create_unit()

    def create_building(self):
        scene = bge.logic.getCurrentScene()
        new_building = Building(scene.addObject('Build', scene.objects['SpawnB']))
        new_building.build_init(self)
