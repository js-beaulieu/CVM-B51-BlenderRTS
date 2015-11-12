from bge import logic, events
import bge
from unit import *

SCROLL_SPEED = 0.25


class Keyboard(object):

    def __init__(self, parent):
        self.parent = parent
        self.events_populate()

    def events_populate(self):
        self.key = {
            "W": logic.keyboard.events[events.WKEY],
            "A": logic.keyboard.events[events.AKEY],
            "S": logic.keyboard.events[events.SKEY],
            "D": logic.keyboard.events[events.DKEY],
            "X": logic.keyboard.events[events.XKEY],
            "Z": logic.keyboard.events[events.ZKEY]
        }

    def key_pressed(self, cont):
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        camX = cam.position[0]
        camY = cam.position[1]
        camZ = cam.position[2]
        self.events_populate()

        # camera movement
        if self.key["W"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY + SCROLL_SPEED, camZ]
        if self.key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY - SCROLL_SPEED, camZ]
        if self.key["S"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY - SCROLL_SPEED, camZ]
        if self.key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY + SCROLL_SPEED, camZ]
        if self.key["W"] == logic.KX_INPUT_ACTIVE and self.key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - SCROLL_SPEED, camY, camZ]
        if self.key["W"] == logic.KX_INPUT_ACTIVE and self.key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX, camY + SCROLL_SPEED, camZ]
        if self.key["S"] == logic.KX_INPUT_ACTIVE and self.key["A"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX, camY - SCROLL_SPEED, camZ]
        if self.key["S"] == logic.KX_INPUT_ACTIVE and self.key["D"] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + SCROLL_SPEED, camY, camZ]

        # keyboard shortcuts
        if self.key["X"] == logic.KX_INPUT_JUST_ACTIVATED:
            bge.c.buildings[0].createUnit()
        if self.key["Z"] == logic.KX_INPUT_JUST_ACTIVATED:
            for i in bge.c.selectedUnits:
                print(i.circle)
            # for i in bge.c.selectedUnits:
                # print(i.id_nb)
