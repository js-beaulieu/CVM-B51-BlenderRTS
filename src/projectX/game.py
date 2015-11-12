import bge
from mouse import *
from keyboard import *
from building import *
from civilisation import *


class Game():

    def __init__(self):
        self.civilisations = []
        self.units = []
        self.selected_units = []
        self.moving_units = []

    def game_init(self):
        self.civilisation = Civilisation()
        self.civilisations.append(self.civilisation)
        self.civilisation.civ_init()

    def game_update(self):
        if self.moving_units:
            for obj in self.moving_units:
                x = obj.worldPosition[0]
                y = obj.worldPosition[1]
                obj.move(x, y)
                if not obj.moving:
                    self.moving_units.remove(obj)


