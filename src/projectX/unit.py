import bge
import math

"""sub-class of a blender game object, keeps all the goodies fonctions of bge KX_GameObject
but add a little twist to it XD (fonctions and variables)"""


class Unit(bge.types.KX_GameObject):

    def __init__(self, parent):  # parent is the old bge object
        self.dmg = 15
        self.speed = 0.1
        self.destination = []
        self.selected = False
        self.circle = None
        self.moving = False
        self.id_nb = "Unit_" + str(bge.c.game.civilisation.buildings[0].count)
        bge.c.game.units.append(self)

    def move(self, x, y):
        """not using the blender sensors and logic brick, thats the python way bitch! :P"""
        if self.destination:
            angle = self.calcAngle(x, y, self.destination[0], self.destination[1])
            pos = self.getAngledPoint(angle, self.speed, x, y)
            self.worldPosition = [pos[0], pos[1], self.position[2]]
            dist = self.calcDistance(x, y, self.destination[0], self.destination[1])
            # if self.selected:
            # self.circle.worldPosition.x = pos[0]
            # self.circle.worldPosition.y = pos[1]
            # self.circle.worldPosition.z = self.position[2]
            if dist < 0.2:
                self.position = self.destination
                self.destination = []
                self.moving = False

    def getAngledPoint(self, angle, longueur, cx, cy):
        x = (math.cos(angle)*longueur)+cx
        y = (math.sin(angle)*longueur)+cy
        return [x, y]

    def calcAngle(self, x1, y1, x2, y2):
        dx = x2-x1
        dy = y2-y1
        angle = (math.atan2(dy, dx))    # % (2*math.pi)) * (180/math.pi)
        return angle

    def calcDistance(self, x1, y1, x2, y2):
        dx = abs(x2-x1)**2
        dy = abs(y2-y1)**2
        distance = math.sqrt(dx + dy)
        return distance

