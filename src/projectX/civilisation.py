import bge
from building import *


class Civilisation():

    def __init__(self):
        self.buildings = []
        self.gold = 1000

    def civ_init(self):
        self.buildings.append(self.create_building())

    def create_building(self):
        scene = bge.logic.getCurrentScene()
        Building(scene.addObject('Build', scene.objects['SpawnB']))
