import bge
from bge import events, render
from mouse import *
from keyboard import *
from game import *
from building import *
from unit import *
from display import *

scene = bge.logic.getCurrentScene()


class Controller():

    def __init__(self, player_nb):
        self.player_id_nb = player_nb
        self.frame = 0
        self.mouse = Mouse(self)
        self.keyboard = Keyboard(self)
        self.display_update = False
        self.ui_panel = 0
        self.button_clicked = 0


def main(cont):
    """called once by the "Always" sensor named InitGame,
    will remove sensors if we have time its kinda complicated"""
    bge.c = Controller(0)  # hard codded, will be the players list index (i++)
    bge.c.game = Game(2)
    bge.c.game.game_init()
    bge.c.display = bgui.bge_utils.System('../../themes/default')
    bge.c.display.load_layout(MainDisplay, None)
    render.showMouse(True)
    render.setMousePosition(400, 400)


def control_update(cont):
    """called every frame by the "Always" sensor named Update
    this is the main loop"""
    bge.c.frame += 1
    bge.c.game.game_update()
    bge.c.display.run()

    if bge.c.button_clicked > 0:
        bge.c.button_clicked -= 1

    if bge.logic.mouse.events:
        bge.c.mouse.select(cont)

    if bge.logic.keyboard.events:
        bge.c.keyboard.key_pressed(cont)

    if not bge.c.game.selected_units:
        bge.c.ui_panel = 4

