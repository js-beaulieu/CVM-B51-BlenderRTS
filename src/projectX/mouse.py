from bge import logic, events, render
from time import clock
from unit import *


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
        self.scene = logic.getCurrentself.scene()
        self.mousePos = cont.sensors["Mouse_Pos"]

        if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT]:
            self.left_click(logic.mouse.events[logic.KX_MOUSE_BUT_LEFT])
        if logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT]:
            self.right_click(logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT])
        if logic.mouse.events[logic.KX_MOUSE_BUT_MIDDLE]:
            self.middle_click(logic.mouse.events[logic.KX_MOUSE_BUT_MIDDLE])

    def left_click(self, event):
        if event == logic.KX_INPUT_JUST_ACTIVATED:
            self.parent.selectedUnits = []
            self.x1 = self.mousePos.hitPosition[0]    # enregistre les coordonees initiales
            self.y1 = self.mousePos.hitPosition[1]

        if event == logic.KX_INPUT_ACTIVE:
            self.x2 = self.mousePos.hitPosition[0]    # enregistre la position actuelle de la souris
            self.y2 = self.mousePos.hitPosition[1]
            z = self.mousePos.hitPosition[2] + 0.1

            render.drawLine((self.x1, self.y1, z), (self.x2, self.y1, z), (1, 0, 0))  # param((point 1), (point 2), (RGB de 0.00 a 1.00)
            render.drawLine((self.x1, self.y1, z), (self.x1, self.y2, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x2, self.y1, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x1, self.y2, z), (1, 0, 0))  # qui dessine le rectangle tant que la souris est positive

        if event == logic.KX_INPUT_JUST_RELEASED:
            total = 0     # sert a tester
            if self.x1 > self.x2:
                p = self.x2
                self.x2 = self.x1
                self.x1 = p

            if self.y1 > self.y2:   # met en ordre croissant
                p = self.y2
                self.y2 = self.y1
                self.y1 = p

            for obj in self.scene.objects:    # itere au travers les objets de la self.scene (pas excellent performances)
                if isinstance(obj, Unit):    # Select = bool in object attributes
                    x = obj.worldPosition[0]
                    y = obj.worldPosition[1]
                    # print("objX = ", x, ", objY = ", y)
                    if x > self.x1 and y > self.y1 and x < self.x2 and y < self.y2:    # si a linterieur du rectangle
                        total += 1
                        self.parent.selectedUnits.append(obj)
            print(total)
            # print("x1 = ", self.x1, ", y1 = ", self.y1, ", x2 = ", self.x2, ", y2 = ", self.y2)

    def right_click(self, event):
        if event == logic.KX_INPUT_JUST_ACTIVATED:
            dist = 0
            for obj in self.parent.selectedUnits:
                obj.destination = [self.mousePos.hitPosition[0] + dist, self.mousePos.hitPosition[1], obj.worldPosition[2]]
                dist += 0.7
                if not obj.moving:
                    self.parent.movingUnits.append(obj)
                    obj.moving = True

    def middle_click(self, event):
        if event == logic.KX_INPUT_JUST_ACTIVATED:
            self.scene.objects['SpawnP'].worldPosition.x = self.mousePos.hitPosition[0] + 1.5  # for isometric cam... weird
            self.scene.objects['SpawnP'].worldPosition.y = self.mousePos.hitPosition[1] - 1
            self.scene.objects['Spawn_Circle'].worldPosition.x = self.mousePos.hitPosition[0]
            self.scene.objects['Spawn_Circle'].worldPosition.y = self.mousePos.hitPosition[1]

    def mouse_movement(self):
        if logic.keyboard.events[events.WKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - CAMERA_SPEED, camY + CAMERA_SPEED, camZ]
        if logic.keyboard.events[events.AKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX - CAMERA_SPEED, camY - CAMERA_SPEED, camZ]
        if logic.keyboard.events[events.SKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + CAMERA_SPEED, camY - CAMERA_SPEED, camZ]
        if logic.keyboard.events[events.DKEY] == logic.KX_INPUT_ACTIVE:
            cam.position = [camX + CAMERA_SPEED, camY + CAMERA_SPEED, camZ]
