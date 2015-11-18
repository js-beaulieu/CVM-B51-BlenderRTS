from bge import logic, events
import bge
from unit import *

SCROLL_SPEED = 0.25


class Keyboard(object):

    def __init__(self, parent):
        self.parent = parent

    def key_pressed(self, cont):
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        camX = cam.position[0]
        camY = cam.position[1]
        camZ = cam.position[2]

        key = {
            "W": logic.keyboard.events[events.WKEY],
            "A": logic.keyboard.events[events.AKEY],
            "S": logic.keyboard.events[events.SKEY],
            "D": logic.keyboard.events[events.DKEY],
            "X": logic.keyboard.events[events.XKEY],
            "Z": logic.keyboard.events[events.ZKEY]
        }

        # camera movement
        if key["W"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY + SCROLL_SPEED, camZ]
        if key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY - SCROLL_SPEED, camZ]
        if key["S"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY - SCROLL_SPEED, camZ]
        if key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY + SCROLL_SPEED, camZ]
        if key["W"] == logic.KX_INPUT_ACTIVE and key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY, camZ]
        if key["W"] == logic.KX_INPUT_ACTIVE and key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX, camY + SCROLL_SPEED, camZ]
        if key["S"] == logic.KX_INPUT_ACTIVE and key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX, camY - SCROLL_SPEED, camZ]
        if key["S"] == logic.KX_INPUT_ACTIVE and key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY, camZ]

        # keyboard shortcuts
        if key["X"] == logic.KX_INPUT_JUST_ACTIVATED:
            bge.c.game.civilisation.buildings[0].create_unit()
        if key["Z"] == logic.KX_INPUT_JUST_ACTIVATED:
            for obj in bge.c.game.bullets:
                print(obj.id_nb)
            # print(bge.c.game.selected_units)
            