import bge
import math

"""sub-class of a blender game object, keeps all the goodies fonctions of bge KX_GameObject
but add a little twist to it XD (fonctions and variables)"""


class Bullet(bge.types.KX_GameObject):

    def __init__(self, parent):  # parent is the old bge object
        self.owner = None
        self.dmg = 15
        self.speed = 0.8
        self.target = None
        self.worldPosition[2] += 0.5
        self.id_nb = bge.c.frame

    def traject_init(self, owner, target, unit):
        self.destination = target.worldPosition
        self.target = target
        self.owner = owner
        self.unit = unit
        self.alert()

    def alert(self):
        x1 = self.target.worldPosition[0]
        y1 = self.target.worldPosition[1]
        for civ in bge.c.game.civilisations:
            if civ != self.owner:
                for i in civ.units:
                    for obj in civ.units[i]:
                        if obj.state == 1:
                            x2 = obj.worldPosition[0]
                            y2 = obj.worldPosition[1]
                            dist = self.calcDistance(x1, y1, x2, y2)
                            if dist < 10:
                                obj.target = self.unit
                                obj.state = 3
    
    def trajectory(self, x, y):
        """param: self, self.worldPosition x, self.worldPosition y"""
        if self.target.hp > 0:
            angle = self.calcAngle(x, y, self.destination[0], self.destination[1])
            pos = self.getAngledPoint(angle, self.speed, x, y)
            self.worldPosition = [pos[0], pos[1], self.worldPosition[2]]
            dist = self.calcDistance(x, y, self.destination[0], self.destination[1])
            if dist < 0.9:
                self.target.hp -= self.dmg
                if self.target.hp <= 0:
                    for i in self.owner.units:
                        for obj in self.owner.units[i]:
                            if obj.state == 3:
                                if obj.target == self.target:
                                    obj.target = None
                                    if not obj.owner.computer:
                                        obj.attacking = False
                    for obj in bge.c.game.bullets:
                        if obj.target == self.target:
                            bge.c.game.bullets.remove(obj)
                            obj.endObject()
                else:
                    bge.c.game.bullets.remove(self)
                    self.endObject()
        else:
            bge.c.game.bullets.remove(self)
            self.endObject()

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


class Zapper(Bullet):

    def __init__(self, parent):
        super(Zapper, self).__init__(parent)
        self.field = 10  # TODO AoE
        self.dmg = 25
        self.speed = 0.7
