from bge import logic, events, render
from unit import *

ZOOM_STEPS = 5
ZOOM_MIN = 10
ZOOM_MAX = 35


class Mouse(object):

    def __init__(self, parent):
        self.parent = parent
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def select(self, cont):
        """ main mouse fonction, will be improved as we add mouse controls
        It is called from bge.c (controller) if mouse.events = True"""
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        mousePos = cont.sensors["Mouse_Pos"]

        if mousePos.position[0] <= 5:
            self.moveCam(1)
            if mousePos.position[0] < 0:
                render.setMousePosition(2, mousePos.position[1])
        elif mousePos.position[1] <= 5:
            self.moveCam(2)
            if mousePos.position[1] < 0:
                render.setMousePosition(mousePos.position[0], 2)
        elif mousePos.position[0] >= render.getWindowWidth() - 5:
            self.moveCam(3)
            if mousePos.position[0] > render.getWindowWidth():
                render.setMousePosition(render.getWindowWidth(), mousePos.position[1] - 2)
        elif mousePos.position[1] >= render.getWindowHeight() - 5:
            self.moveCam(4)
            if mousePos.position[1] > render.getWindowHeight():
                render.setMousePosition(mousePos.position[0], render.getWindowHeight() - 2)

        if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_ACTIVATED:
            self.parent.selectedUnits = []
            self.x1 = mousePos.hitPosition[0]    # enregistre les coordonees initiales
            self.y1 = mousePos.hitPosition[1]

        if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_ACTIVE:
            self.x2 = mousePos.hitPosition[0]    # enregistre la position actuelle de la souris
            self.y2 = mousePos.hitPosition[1]
            z = mousePos.hitPosition[2] + 0.1

            render.drawLine((self.x1, self.y1, z), (self.x2, self.y1, z), (1, 0, 0))
            render.drawLine((self.x1, self.y1, z), (self.x1, self.y2, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x2, self.y1, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x1, self.y2, z), (1, 0, 0))

        if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_RELEASED:
            total = 0     # sert a tester
            if self.x1 > self.x2:
                p = self.x2
                self.x2 = self.x1
                self.x1 = p

            if self.y1 > self.y2:   # met en ordre croissant
                p = self.y2
                self.y2 = self.y1
                self.y1 = p

            for obj in scene.objects:    # itere au travers les objets de la scene (pas excellent performances)
                if isinstance(obj, Unit):    # Select = bool in object attributes
                    if obj not in bge.c.units:
                        self.parent.units.append(obj)

                    x = obj.worldPosition[0]
                    y = obj.worldPosition[1]

                    if x > self.x1 and y > self.y1 and x < self.x2 and y < self.y2:    # si a linterieur du rectangle
                        total += 1
                        self.parent.selectedUnits.append(obj)
                        #obj.circle = scene.addObject('Select_Circle', obj)
                        obj.selected = True

        if logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT] == logic.KX_INPUT_JUST_ACTIVATED:
            dist = 0
            for obj in self.parent.selectedUnits:
                obj.destination = [mousePos.hitPosition[0] + dist, mousePos.hitPosition[1], obj.worldPosition[2]]
                dist += 0.7
                if not obj.moving:
                    self.parent.movingUnits.append(obj)
                    obj.moving = True

        if logic.mouse.events[logic.KX_MOUSE_BUT_MIDDLE] == logic.KX_INPUT_JUST_ACTIVATED:
            scene.objects['Way_Circle'].worldPosition.x = mousePos.hitPosition[0]
            scene.objects['Way_Circle'].worldPosition.y = mousePos.hitPosition[1]
            bge.c.buildings[0].way_point = True
            scene.objects['Way_Circle'].setVisible(True)

        if logic.mouse.events[events.WHEELDOWNMOUSE] == logic.KX_INPUT_JUST_ACTIVATED:
            cam = scene.cameras["Camera"]
            if cam.ortho_scale <= ZOOM_MAX:
                for i in range(ZOOM_STEPS):
                    cam.ortho_scale += 1

        if logic.mouse.events[events.WHEELUPMOUSE] == logic.KX_INPUT_JUST_ACTIVATED:
            cam = scene.cameras["Camera"]
            if cam.ortho_scale >= ZOOM_MIN:
                for i in range(ZOOM_STEPS):
                    cam.ortho_scale -= 1

    def moveCam(self, side):
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        camX = cam.position[0]
        camY = cam.position[1]
        camZ = cam.position[2]
        if side == 1:
            cam.position = [camX - 0.1, camY - 0.1, camZ]
        elif side == 2:
            cam.position = [camX - 0.1, camY + 0.1, camZ]
        elif side == 3:
            cam.position = [camX + 0.1, camY + 0.1, camZ]
        elif side == 4:
            cam.position = [camX + 0.1, camY - 0.1, camZ]

