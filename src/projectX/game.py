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
        self.selected_units = []
        self.moving_units = []

    def game_init(self):
        scene = bge.logic.getCurrentScene()
        self.civilisation = Civilisation()
        self.civilisations.append(self.civilisation)
        self.civilisation.civ_init()
        Mine(scene.addObject('Mine', scene.objects['SpawnM']))

    def game_update(self):
        for obj in self.units:
            obj.act()


