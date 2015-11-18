import bge
import math
from bullet import *

"""sub-class of a blender game object, keeps all the goodies fonctions of bge KX_GameObject
but add a little twist to it XD (fonctions and variables)"""


class Unit(bge.types.KX_GameObject):

    def __init__(self, parent):  # parent is the old bge object
        self.dmg = 15
        self.hp = 45
        self.field = 10
        self.speed = 0.1
        self.att_spd = 80
        self.harv_chrono = 0
        self.harv_dest = []
        self.harv_mine = None
        self.att_chrono = 0
        self.destination = []
        self.selected = False
        self.moving = False
        self.harvesting = False
        self.attacking = False
        self.standing = False
        self.id_nb = "Unit_" + str(bge.c.game.civilisation.buildings[0].count)
        bge.c.game.units.append(self)

    def act(self):
        """param: self"""
        if self.selected:
            self.children['Select_Circle'].visible = True
        else:
            self.children['Select_Circle'].visible = False
        x = self.worldPosition[0]
        y = self.worldPosition[1]
        if self.moving:
            self.move(x, y)
        if self.attacking and self.target:
            self.attack(x, y)
        if self.harvesting:
            self.harvest(x, y)
        else:
            pass

    def move(self, x, y):
        """param: self, self.worldPosition x, self.worldPosition y"""
        if self.destination:
            angle = self.calcAngle(x, y, self.destination[0], self.destination[1])
            pos = self.getAngledPoint(angle, self.speed, x, y)
            self.worldPosition = [pos[0], pos[1], self.position[2]]
            dist = self.calcDistance(x, y, self.destination[0], self.destination[1])
            if dist < 0.2:
                self.position = self.destination
                self.destination = []
                self.moving = False

    def attack(self, x, y):
        """param: self, self.worldPosition x, self.worldPosition y"""
        if self.target:
            self.destination = self.target.worldPosition
            dist = self.calcDistance(x, y, self.destination[0], self.destination[1])
            if dist > self.field:
                self.move(x, y)
            elif self.att_chrono != self.att_spd:
                self.att_chrono += 1
            elif self.att_chrono == self.att_spd:
                scene = bge.logic.getCurrentScene()
                pew = Bullet(scene.addObject('Bullet', self))
                pew.owner = self
                bge.c.game.bullets.append(pew)
                pew.target = self.target
                pew.traject_init()
                self.att_chrono = 0

    def harvest(self, x, y):
        """param: self, self.worldPosition x, self.worldPosition y"""
        dist = self.calcDistance(x, y, self.destination[0], self.destination[1])
        if dist > 2:
            self.move(x, y)
        elif self.harv_chrono != 140:
            self.harv_chrono += 1
        elif self.harv_chrono == 140:
            if self.destination == self.harv_dest:
                self.harv_mine.material -= 10
                self.destination = bge.c.game.civilisation.buildings[0].worldPosition  # hard codded, TODO
                self.harv_chrono = 0
            elif self.destination != self.harv_dest:
                bge.c.game.civilisation.gold += 10  # hard codded, TODO
                self.destination = self.harv_dest
                self.harv_chrono = 0

    def getAngledPoint(self, angle, longueur, cx, cy):
        """param: self, self.calcAngle(), self.speed, self.worldPosition x, self.worldPosition y"""
        x = (math.cos(angle)*longueur)+cx
        y = (math.sin(angle)*longueur)+cy
        return [x, y]

    def calcAngle(self, x1, y1, x2, y2):
        """param: self, self.worldPosition x, self.worldPosition y, self.destination x, self.destination y"""
        dx = x2-x1
        dy = y2-y1
        angle = (math.atan2(dy, dx))    # % (2*math.pi)) * (180/math.pi)
        return angle

    def calcDistance(self, x1, y1, x2, y2):
        """param: self, self.worldPosition x, self.worldPosition y, self.destination x, self.destination y"""
        dx = abs(x2-x1)**2
        dy = abs(y2-y1)**2
        distance = math.sqrt(dx + dy)
        return distance

