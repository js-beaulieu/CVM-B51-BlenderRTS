from bge import logic, events
import bge


class Keyboard(object):

    def __init__(self, parent):
        self.parent = parent

    def key_pressed(self, cont):
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        camX = cam.position[0]
        camY = cam.position[1]
        camZ = cam.position[2]
        mousePos = cont.sensors["Mouse_Pos"]

        if logic.keyboard.events[events.XKEY] == logic.KX_INPUT_JUST_ACTIVATED:
            bge.c.addO()
        if logic.keyboard.events[events.ZKEY] == logic.KX_INPUT_JUST_ACTIVATED:
            for obj in bge.c.selectedUnits:
                print(obj.id_nb)
        if logic.keyboard.events[events.WKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - 0.1, camY + 0.1, camZ]
        if logic.keyboard.events[events.AKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - 0.1, camY - 0.1, camZ]
        if logic.keyboard.events[events.SKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + 0.1, camY - 0.1, camZ]
        if logic.keyboard.events[events.DKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + 0.1, camY + 0.1, camZ]
        
