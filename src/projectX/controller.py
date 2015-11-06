import bge
from bge import events, render
from mouse import *
from keyboard import *

scene = bge.logic.getCurrentScene()


class Controller():

    def __init__(self):
        self.frame = 0
        self.mouse = Mouse(self)
        self. keyboard = Keyboard(self)
        self.x = 0  # is used for testing purpose in addO()
        self.y = 0  # is used for testing purpose in addO()
        self.selectedUnits = []
        self.movingUnits = []
        self.count = 0

    def addO(self):
        """ Temporary fonction used to test the controller, the spawn point move,
        the subclassing of blender game objects and spawning them, well, it actually test everything ^^"""
        scene = bge.logic.getCurrentScene()
        scene.addObject('Unit', scene.objects['SpawnP'])
        self.count += 1


def main():
    """called once by the "Always" sensor named InitGame,
    will remove sensors if we have timeits kinda complicated"""
    bge.c = Controller()
    scene.addObject('Build', scene.objects['SpawnB'])
    



def update(cont):
    """called every frame by the "Always" sensor named Update
    this is the main loop"""
    bge.c.frame += 1
    render.showMouse(True)
    if bge.logic.mouse.events:
        bge.c.mouse.select(cont)

    if bge.logic.keyboard.events:
        bge.c.keyboard.key_pressed(cont)

    if bge.c.movingUnits:
        for obj in bge.c.movingUnits:
            x = obj.worldPosition[0]
            y = obj.worldPosition[1]
            obj.move(x, y)
