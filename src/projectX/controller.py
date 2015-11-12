import bge
from bge import events, render
from mouse import *
from keyboard import *
from building import *
from display import *
from test import *

scene = bge.logic.getCurrentScene()


class Controller():

    def __init__(self):
        self.frame = 0
        self.display = bgui.bge_utils.System('../../themes/default')
        self.display.load_layout(Display, None)
        self.mouse = Mouse(self)
        self.keyboard = Keyboard(self)
        self.buildings = []
        self.units = []
        self.selectedUnits = []
        self.movingUnits = []
        self.selectCircles = []
        self.count = 0
        self.gold = 1000


def main():
    """called once by the "Always" sensor named InitGame,
    will remove sensors if we have time its kinda complicated"""
    bge.c = Controller()
    render.showMouse(True)
    render.setMousePosition(300, 300)
    Building(scene.addObject('Build', scene.objects['SpawnB']))


def update(cont):
    """called every frame by the "Always" sensor named Update
    this is the main loop"""
    bge.c.frame += 1
    bge.c.display.run()
    if bge.logic.mouse.events:
        bge.c.mouse.select(cont)

    if bge.logic.keyboard.events:
        bge.c.keyboard.key_pressed(cont)

    if bge.c.movingUnits:
        for obj in bge.c.movingUnits:
            x = obj.worldPosition[0]
            y = obj.worldPosition[1]
            obj.move(x, y)
            if not obj.moving:
                bge.c.movingUnits.remove(obj)
