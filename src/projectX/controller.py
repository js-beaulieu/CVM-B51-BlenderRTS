import bge
from bge import events, render
from mouse import *
from keyboard import *
from game import *
from building import *
from display import *
from test import *

scene = bge.logic.getCurrentScene()


class Controller():

    def __init__(self):
        self.frame = 0
        self.mouse = Mouse(self)
        self.keyboard = Keyboard(self)


def main(cont):
    """called once by the "Always" sensor named InitGame,
    will remove sensors if we have time its kinda complicated"""
    bge.c = Controller()
    bge.c.game = Game()
    bge.c.game.game_init()
    bge.c.display = bgui.bge_utils.System('../../themes/default')
    bge.c.display.load_layout(MainDisplay, None)
    render.showMouse(True)
    render.setMousePosition(400, 400)
    # cont.sensors["Update"].active = True


def control_update(cont):
    """called every frame by the "Always" sensor named Update
    this is the main loop"""
    bge.c.frame += 1
    bge.c.game.game_update()
    #bge.c.display.update()
    #bge.c.display.goldLbl.text='Gold = ' + str(bge.c.game.civilisation.gold)
    bge.c.display.run()

    if bge.logic.mouse.events:
        bge.c.mouse.select(cont)

    if bge.logic.keyboard.events:
        bge.c.keyboard.key_pressed(cont)

